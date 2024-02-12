import random
import time

WIDTH = 1024
HEIGHT = 480

class Monster(Actor):

    def __init__(self, x: int, y: int):
        self.is_lopende = False
        self.is_kapot = False
        super().__init__(self.geef_plaatje())
        self.step = 0
        self.x = x
        self.y = y

    def geef_plaatje(self):
        raise NotImplementedError("methode geef_plaatje is niet geimplementeerd")

    def ga_een_kant_op(self, pixels: int):
        raise NotImplementedError("methode ga_een_kant_op is niet geimplementeerd")

    def neem_stap(self):
        self.step = self.step + 1
        if self.step > 7:
            self.step = 0
        # Zijn we nog aan het lopen? Neem dan over een seconde nog een stap
        self.ga_een_kant_op(pixels=5)
        if self.is_lopende:
            clock.schedule_unique(self.neem_stap, 0.1)

    def wissel_lopen(self):
        self.is_lopende = not self.is_lopende
        if self.is_lopende:
            self.neem_stap()

    def start_lopen(self):
        if not self.is_lopende:
            self.wissel_lopen()

    def stop_lopen(self):
        if self.is_lopende:
            self.wissel_lopen()

    def draw(self):
        self.image = self.geef_plaatje()
        super().draw()

    def ga_links(self, pixels: int):
        if self.x - pixels < 0:
            self.x = 0
        else:
            self.x = self.x - pixels

    def ga_rechts(self, pixels: int):
        if self.x + pixels > WIDTH:
            self.x = WIDTH
        else:
            self.x = self.x + pixels

    def ga_omhoog(self, pixels: int):
        if self.y - pixels < 0:
            self.y = 0
        else:
            self.y = self.y - pixels

    def ga_omlaag(self, pixels: int):
        if self.y + pixels > HEIGHT:
            self.y = HEIGHT
        else:
            self.y = self.y + pixels

class Zombie(Monster):

    def ga_een_kant_op(self, pixels: int):
        # Zombies blijven bewegen ook al zijn ze kapot... het zijn zombies
        # Willekeurig omhoog(1), omlaag(2), links(3) of rechts(4), Nietsdoen (5)
        richting = random.randint(1, 5)
        # Controleer welke richting is gekozen
        if richting == 1:
            self.ga_omhoog(pixels)
        elif richting == 2:
            self.ga_omlaag(pixels)
        elif richting == 3:
            self.ga_links(pixels)
        elif richting == 4:
            self.ga_rechts(pixels)

    def geef_plaatje(self):
        if self.is_kapot:
            return 'zombie_hurt'
        if self.is_lopende:
            return 'zombie_walk_' + str(self.step)
        return 'zombie_idle'

class Robot(Monster):

    def ga_een_kant_op(self, pixels: int):
        # Als we kapot zijn doen we niets als robot
        if self.is_kapot:
            return
        # Robots besluiten altijd naar de dichtsbijzijnde hoek te gaan tenzij ze daar al zijn en anders teleporten ze weer naar het midden
        if self.x <= WIDTH / 2 and self.x > 0:
            self.ga_omhoog(pixels)
        if self.x > WIDTH / 2 and self.x < WIDTH:
            self.ga_omlaag(pixels)
        if self.y <= HEIGHT / 2 and self.y > 0:
            self.ga_links(pixels)
        if self.y > HEIGHT / 2 and self.y < HEIGHT:
             self.ga_rechts(pixels)

        # Een robot aan de rand teleporteert naar een willekeurige locatie
        if(self.x <= 0 or self.x >= WIDTH or self.y <= 0 or self.y >= HEIGHT):
            self.x = random.randint(50, WIDTH - 50)
            self.y = random.randint(50, HEIGHT - 50)

    def geef_plaatje(self):
        if self.is_kapot:
            return 'robot_hurt'
        if self.is_lopende:
            return 'robot_walk_' + str(self.step)
        return 'robot_idle'

class Avonturier(Monster):

    def ga_een_kant_op(self, pixels: int):
        # Als we kapot zijn doen we niets als Avonturier
        if self.is_kapot:
            return
        # Willekeurig omhoog(1), omlaag(2), links(3) of rechts(4), Nietsdoen (5)
        richting = random.randint(1, 5)
        # Controleer welke richting is gekozen
        if richting == 1:
            self.ga_omhoog(pixels)
        elif richting == 2:
            self.ga_omlaag(pixels)
        elif richting == 3:
            self.ga_links(pixels)
        elif richting == 4:
            self.ga_rechts(pixels)

    def geef_plaatje(self):
        if self.is_kapot:
            return 'adventurer_hurt'
        if self.is_lopende:
            return 'adventurer_walk_' + str(self.step)
        return'adventurer_idle'


class Horde:

    def start(self):
        for monster in self.items:
            monster.start_lopen()

    def draw(self):
        for monster in self.items:
            monster.draw()

    def check_hit(self, pos):
        for monster in self.items:
            if (monster.collidepoint(pos)):
                monster.is_kapot = True

    def is_alles_kapot(self):
        return all(monster.is_kapot for monster in self.items)

class HordeMonsters(Horde):
    def __init__(self, aantal_robots: int, aantal_zombies: int):
        self.items = list()
        for i in range(1, aantal_robots, 1):
            self.items.append(Robot(random.randint(1, WIDTH), random.randint(1, HEIGHT)))
        for i in range(1, aantal_zombies, 1):
            self.items.append(Zombie(random.randint(1, WIDTH), random.randint(1, HEIGHT)))

class HordeAvonturiers(Horde):
    def __init__(self, aantal_avonturiers: int):
        self.items = list()
        for i in range(1, aantal_avonturiers, 1):
            self.items.append(Avonturier(random.randint(1, WIDTH), random.randint(1, HEIGHT)))


start_tijd = time.time()
monsters = HordeMonsters(aantal_robots= 5, aantal_zombies= 5)
monsters.start()

avonturiers = HordeAvonturiers(aantal_avonturiers= 10)
avonturiers.start()

definitieve_tijd = 0
wacht_tijd = 1

def draw():
    global definitieve_tijd

    huidige_tijd = time.time()
    verlopen_tijd = (huidige_tijd - start_tijd - wacht_tijd)

    if(verlopen_tijd < 0 ):
        screen.fill((0, 0, 0))
        screen.draw.text("Maak je klaar!" , midtop=(WIDTH / 2, HEIGHT / 4), color="green", fontsize=60)
        bericht = "{:.2f}".format(abs(verlopen_tijd))
        screen.draw.text(bericht , midtop=(WIDTH / 2, HEIGHT / 2), color="green", fontsize=120)

    elif monsters.is_alles_kapot():
        if definitieve_tijd == 0:
            definitieve_tijd = verlopen_tijd
        screen.fill((0, 255, 0))
        bericht = "Gewonnen in {:.2f} seconden".format(definitieve_tijd)
        screen.draw.text(bericht , midtop=(WIDTH / 2, HEIGHT / 2), color="black", fontsize=60)
    elif avonturiers.is_alles_kapot():
        if definitieve_tijd == 0:
            definitieve_tijd = verlopen_tijd
        screen.fill((255, 0, 0))
        bericht = "Oh oh, Verloren! \n\n Tijd: {:.2f} seconden".format(definitieve_tijd)
        screen.draw.text(bericht , midtop=(WIDTH / 2, HEIGHT / 3), color="black", fontsize=60)
    else:
        screen.fill((255, 255, 255))
        monsters.draw()
        avonturiers.draw()
        status_bericht = "Verlopen tijd: {:.2f} seconden".format(verlopen_tijd)
        screen.draw.text(status_bericht , midtop=(WIDTH / 2, 0), color="orange")


def update():
    # Update wordt iedere keer dat het scherm weergegeven wordt aangeroepen
    pass

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        monsters.check_hit(pos)
        avonturiers.check_hit(pos)
