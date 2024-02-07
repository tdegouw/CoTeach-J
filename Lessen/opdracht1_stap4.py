import random

WIDTH = 1024
HEIGHT = 480

class Character(Actor):

    def __init__(self, character_type: str, x: int, y: int):
        self.character_type = character_type
        self.moving = False
        super().__init__(self.geef_plaatje())
        self.step = 0
        self.x = x
        self.y = y

    def geef_plaatje(self):
        if self.moving:
            return self.character_type + '_walk_' + str(self.step)
        return self.character_type + '_idle'

    def neem_stap(self):
        self.step = self.step + 1
        if self.step > 7:
            self.step = 0
        # Zijn we nog aan het lopen? Neem dan over een seconde nog een stap
        if self.moving:
            clock.schedule_unique(self.neem_stap, 0.1)

    def wissel_lopen(self):
        self.moving = not self.moving
        if self.moving:
            self.neem_stap()

    def start_lopen(self):
        if not self.moving:
            self.wissel_lopen()

    def stop_lopen(self):
        if self.moving:
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

class RobotHorde():

    def __init__(self, aantal: int):
        self.robots = list()
        for i in range(1, aantal, 1):
            self.robots.append(Character('robot', i * 100, 56))

    def neem_stap(self):
        for robot in self.robots:
            robot.ga_een_kant_op(pixels=5)
        clock.schedule_unique(self.neem_stap, 0.1)

    def start(self):
        for robot in self.robots:
            robot.start_lopen()
        clock.schedule_unique(self.neem_stap, 0.1)

    def draw(self):
        for robot in self.robots:
            robot.draw()


horde = RobotHorde(10)
horde.start()

def draw():
    screen.fill((255, 255, 255))
    horde.draw()

def update():
    pass

def on_mouse_down(pos, button):
    pass

