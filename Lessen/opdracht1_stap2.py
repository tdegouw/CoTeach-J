WIDTH = 512
HEIGHT = 256

# Opdracht: Je ziet dat de robot hard rent als je iedere update een
# stap zet. Probeer het eens door gebruik te maken van asynchroniteit
# in de code, in dit geval door gebruik te maken van de clock / scheduler
#
# https://pygame-zero.readthedocs.io/en/stable/builtins.html#clock
#

class Robot(Actor):

    def __init__(self):
        self.is_lopende = False
        self.step = 0
        super().__init__(self.geef_plaatje(), (100, 56))

    def geef_plaatje(self):
        if self.is_lopende:
            self.step = self.step + 1
            if self.step > 7:
                self.step = 0
            return 'robot_walk_' + str(self.step)
        return 'robot_idle'

    def wissel_lopen(self):
        self.is_lopende = not self.is_lopende

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
