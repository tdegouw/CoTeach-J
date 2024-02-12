WIDTH = 512
HEIGHT = 256

# Opdracht:
#
# De robot loopt nu wel, maar hij beweegt nog niet over het scherm.
# Kijk eens of je de robot willekeurig over het scherm kunt laten bewegen
# op het moment dat deze begint te lopen door deze bij iedere stap een
# beweging naar een willekeurige kant op te laten doen.

class Robot(Actor):

    def __init__(self):
        self.is_lopende = False
        self.step = 0
        super().__init__(self.geef_plaatje())

    def geef_plaatje(self):
        if self.is_lopende:
            return 'robot_walk_' + str(self.step)
        return 'robot_idle'

    def neem_stap(self):
        self.step = self.step + 1
        if self.step > 7:
            self.step = 0
        if self.is_lopende:
            clock.schedule_unique(self.neem_stap, 0.1)

    def wissel_lopen(self):
        self.is_lopende = not self.is_lopende
        if self.is_lopende:
            self.neem_stap()

    def draw(self):
        self.image = self.geef_plaatje()
        super().draw()

robot = Robot()

def draw():
    screen.fill((255, 255, 255))
    robot.draw()

def update():
    pass

def on_mouse_down(pos, button):
    if button == mouse.LEFT and robot.collidepoint(pos):
        robot.wissel_lopen()

