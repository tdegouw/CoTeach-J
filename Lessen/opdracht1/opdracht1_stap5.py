from print_object import print_object
import random

WIDTH = 512
HEIGHT = 256

# Opdracht: Modulariseren
#
# 2 monsters is leuk maar kijk eens of je nu een
# class kunt maken die meerdere monsters maakt en allemaal
# op een andere plek op het scherm zet. Noem deze class een 'Horde' of 'Zwerm'.
#
# Tips: Je kunt een list() gebruiken om monsters in op te slaan
# en door heen te lopen. Kijk eens of je het aantal aan te maken
# zombies en robots als parameter kunt meegeven
#
# een list maak je door bijvoorbeeld
#
# monsters = list()
#
# vervolgens voeg je een monster toe aan de list
#
# monsters.append(Zombie())
#
# Om vervolgens weer door alle monsters heen te lopen kun je de lijst enumereren en id
# aanroepen om het geheugen adres van het object te zien
#
# for monster in monsters:
#       print(id(monster))
#       monster.doe_je_ding()
#
# Doel van de opdracht: Begrijpen dat objecten altijd doorgegeven worden door
# middel van verwijzingen naar het geheugen en niet door de waarde door te geven
#
# Geavanceerde opdracht:
#
# Kijk eens of je muisklik nog werkt. Hoe zou je het oplossen als je nu een voor een
# de monsters zou willen aanklikken om ze te stoppen?
#

class Monster(Actor):

    def __init__(self):
        self.is_lopende = False
        super().__init__(self.geef_plaatje(), (100,45))
        self.step = 0


    def geef_plaatje(self):
        raise NotImplementedError('methode geef_plaatje is niet geimplementeerd')

    def neem_stap(self):
        self.step = self.step + 1
        if self.step > 7:
            self.step = 0
        # Zijn we nog aan het lopen? Neem dan over een seconde nog een stap
        self.ga_een_kant_op(pixels = 5)
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
            return 'zombie_walk_' + str(self.step)
        return'zombie_idle'

class Robot(Monster):

    def geef_plaatje(self):
        if self.is_lopende:
            return 'robot_walk_' + str(self.step)
        return'robot_idle'

robot = Robot()
robot.start_lopen()
print_object(robot)

zombie = Zombie()
zombie.start_lopen()
zombie.x = 200
print_object(zombie)

def draw():
    screen.fill((255, 255, 255))
    robot.draw()
    zombie.draw()

def update():
    pass

def on_mouse_down(pos, button):
    if button == mouse.LEFT and robot.collidepoint(pos):
        robot.wissel_lopen()

    if button == mouse.LEFT and zombie.collidepoint(pos):
        zombie.wissel_lopen()
