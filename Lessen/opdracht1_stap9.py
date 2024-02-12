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

    def ga_een_kant_op(self, pixels: int):
        # Als we is_kapot zijn doen we niets
        if self.is_kapot:
            return
        # Willekeurig omhoog(1), omlaag(2), links(3) of rechts(4), Nietsdoen (5)
        richting = random.randint(1, 5)
        # Controleer welke richting is gekozen
        if richting == 1:
            if self.x - pixels < 0:
                self.x = 0
            else:
                self.x = self.x - pixels
        elif richting == 2:
            if self.x + pixels > WIDTH:
                self.x = WIDTH
            else:
                self.x = self.x + pixels
        elif richting == 3:
            if self.y - pixels < 0:
                self.y = 0
            else:
                self.y = self.y - pixels
        elif richting == 4:
            if self.y + pixels > HEIGHT:
                self.y = HEIGHT
            else:
                self.y = self.y + pixels

class Zombie(Monster):

    def geef_plaatje(self):
        if self.is_kapot:
            return 'zombie_hurt'
        if self.is_lopende:
            return 'zombie_walk_' + str(self.step)
        return'zombie_idle'

class Robot(Monster):

    def geef_plaatje(self):
        if self.is_kapot:
            return 'robot_hurt'
        if self.is_lopende:
            return 'robot_walk_' + str(self.step)
        return'robot_idle'

class Avonturier(Monster):

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

    def is_iemand_levend(self):
        iemand_in_leven = False
        for monster in self.items:
            if not monster.is_kapot:
                iemand_in_leven = True

        return iemand_in_leven

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
wacht_tijd = 2

def draw():
    global definitieve_tijd

    huidige_tijd = time.time()
    verlopen_tijd = (huidige_tijd - start_tijd - wacht_tijd)

    if(verlopen_tijd < 0 ):
        screen.fill((0, 0, 0))
        screen.draw.text("Maak je klaar!" , midtop=(WIDTH / 2, HEIGHT / 4), color="green", fontsize=60)
        bericht = "{:.2f}".format(abs(verlopen_tijd))
        screen.draw.text(bericht , midtop=(WIDTH / 2, HEIGHT / 2), color="green", fontsize=120)

    elif not monsters.is_iemand_levend():
        if definitieve_tijd == 0:
            definitieve_tijd = verlopen_tijd
        screen.fill((0, 255, 0))
        bericht = "Gewonnen in {:.2f} seconden".format(definitieve_tijd)
        screen.draw.text(bericht , midtop=(WIDTH / 2, HEIGHT / 2), color="black", fontsize=60)
    elif not avonturiers.is_iemand_levend():
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
    pass

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        monsters.check_hit(pos)
        avonturiers.check_hit(pos)