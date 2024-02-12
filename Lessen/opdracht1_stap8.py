import random
import time

WIDTH = 1024
HEIGHT = 480

# Eindopdracht:
#
# En om het wat moeilijker te maken willen we graag ook een horde aan
# avonturiers. De opdracht is om alle monsters op het scherm zo snel mogelijk
# weg te klikken voordat alle avonturiers weggeklikt zijn (per ongeluk).
#
# Kijk wat je nog kunt doen om het rondlopen extra complex te maken, maak
# de game lastig!
#
# Doel van de opdracht: Alles samenvoegen en een game maken




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


class Horde:
    def __init__(self, aantal_robots: int, aantal_zombies: int):
        self.monsters = list()
        for i in range(1, aantal_robots, 1):
            self.monsters.append(Robot(i * 150, 56))
        for i in range(1, aantal_zombies, 1):
            self.monsters.append(Zombie(i * 150, 250))

    def start(self):
        for monster in self.monsters:
            monster.start_lopen()

    def draw(self):
        for monster in self.monsters:
            monster.draw()

    def check_hit(self, pos):
        for monster in self.monsters:
            if (monster.collidepoint(pos)):
                monster.is_kapot = True

    # class method
    def is_kapot(self):
        return all(monster.is_kapot for monster in self.monsters)

# globale functie
def is_kapot(self):
    return all(monster.is_kapot for monster in horde.monsters)

def decide_movement(movement_algorithm):
    def wrapper(monster, target_x, target_y):
        return movement_algorithm(monster, target_x, target_y)
    return wrapper


start_tijd = time.time()
horde = Horde(aantal_robots=5, aantal_zombies=5)
horde.start()

definitieve_tijd = 0

def draw():
    global definitieve_tijd
    huidige_tijd = time.time()
    verlopen_tijd = (huidige_tijd - start_tijd)
    # Als alles kapot is,
    if is_kapot(horde):
        if definitieve_tijd == 0:
            definitieve_tijd = verlopen_tijd
        screen.fill((0, 0, 0))
        win_bericht = "Horde verslagen in {:.2f} seconden".format(definitieve_tijd)
        screen.draw.text(win_bericht , midtop=(WIDTH / 2, HEIGHT / 2), color="orange", fontsize=60)
    else:
        screen.fill((255, 255, 255))
        horde.draw()
        status_bericht = "Verlopen tijd: {:.2f} seconden".format(verlopen_tijd)
        screen.draw.text(status_bericht , midtop=(WIDTH / 2, 0), color="orange")


def update():
    pass

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        horde.check_hit(pos)

