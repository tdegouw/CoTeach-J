import random

WIDTH = 1024
HEIGHT = 480

# Opdracht: een extra status toevoegen
#
# Nu lijkt het al meer op een spel. Geef de monsters nu de mogelijkheid om kapot te gaan. Hiervoor
# is een plaatje robot_hurt en zombie_hurt aanwezig.
#
# Vraag: Zou je in plaats van attributen ook een extra object kunnen gebruiken om dit te doen?
#
# Doel van de opdracht: zelfstandig attributen toevoegen
#


class Monster(Actor):
    def __init__(self, x, y):
        self.is_lopende = False
        super().__init__(self.geef_plaatje(), (x, y))
        self.step = 0

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
        if self.is_lopende:
            return "zombie_walk_" + str(self.step)
        return "zombie_idle"


class Robot(Monster):
    def geef_plaatje(self):
        if self.is_lopende:
            return "robot_walk_" + str(self.step)
        return "robot_idle"


class Horde:
    def __init__(self, aantal_robots: int, aantal_zombies: int):
        self.monsters = list()
        for i in range(1, aantal_robots, 1):
            self.monsters.append(Robot(i * 100, 56))
        for i in range(1, aantal_zombies, 1):
            self.monsters.append(Zombie(i * 100, 150))

    def start(self):
        for monster in self.monsters:
            print(id(monster))
            monster.start_lopen()

    def draw(self):
        for monster in self.monsters:
            monster.draw()

    def check_hit(self, pos):
        for monster in self.monsters:
            if (monster.collidepoint(pos)):
                monster.wissel_lopen()

horde = Horde(aantal_robots=5, aantal_zombies=5)
horde.start()


def draw():
    screen.fill((255, 255, 255))
    horde.draw()

def update():
    # Update wordt iedere keer dat het scherm weergegeven wordt aangeroepen
    pass

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        horde.check_hit(pos)

