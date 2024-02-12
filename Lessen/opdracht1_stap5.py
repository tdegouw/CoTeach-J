import random

WIDTH = 512
HEIGHT = 256

# Opdracht 5:
#
# 1 Robot is leuk, maar kijk eens of je nu een
# class kunt maken die meerdere robots maakt en allemaal
# op een andere plek op het scherm zet.
#
# Tips: Je kunt een list() gebruiken om robots in op te slaan
# en door heen te lopen. Kijk eens of je het aantal aan te maken
# robots als parameter kunt meegeven

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

zombie = Zombie()
zombie.start_lopen()

def draw():
    screen.fill((255, 255, 255))
    robot.draw()
    zombie.draw()

def update():
    pass

def on_mouse_down(pos, button):
    pass

