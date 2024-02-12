import random
import time

WIDTH = 1024
HEIGHT = 480

# Opdracht: pure functies
#
# Nu is het ook leuk als het spel echt eindigt als je alle robots/zombies kapot hebt gemaakt
# kijk eens of je een eindscherm kunt maken als alle robots/zombies weg zijn. Doe dit door
# middel van een globale pure functie die als argument een horde krijgt en als resultaat
# een boolean om te controleren of er nog een monster in de horde zit die nog niet kapot is.
#
# Doel van de opdracht: zien wat pure functies zijn en hoe je deze kunt gebruiken in
# combinatie met objecten
#
# Vervolg opdracht:
#
# Kijk eens of je de zombies kunt laten blijven bewegen nadat ze aangeklikt zijn, hoe zou je
# dit oplossen?
#
# Vervolg opdracht:
#
# Het is wat saai dat alle monsters hetzelfde lopen. Kijk eens of je de robots naar de
# rand van het scherm kunt laten lopen en op een willekeurige plek in het speelveld kunt
# plaatsen als deze daar aangekomen is.

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
            return "zombie_hurt"
        if self.is_lopende:
            return "zombie_walk_" + str(self.step)
        return "zombie_idle"


class Robot(Monster):
    def geef_plaatje(self):
        if self.is_kapot:
            return "robot_hurt"
        if self.is_lopende:
            return "robot_walk_" + str(self.step)
        return "robot_idle"


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
            if monster.collidepoint(pos):
                monster.is_kapot = True



start_tijd = time.time()
horde = Horde(aantal_robots=5, aantal_zombies=5)
horde.start()


def draw():
    huidige_tijd = time.time()
    verlopen_tijd = huidige_tijd - start_tijd
    screen.fill((255, 255, 255))
    horde.draw()
    status_bericht = "Verlopen tijd: {:.2f} seconden".format(verlopen_tijd)
    screen.draw.text(status_bericht, midtop=(WIDTH / 2, 0), color="orange")


def update():
    # Update wordt iedere keer dat het scherm weergegeven wordt aangeroepen
    pass

def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        horde.check_hit(pos)
