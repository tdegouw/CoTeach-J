WIDTH = 512
HEIGHT = 256

# Opdracht: Kijk of het lukt om het plaatje te laten wisselen
# om de robot te laten lopen. Er zijn 7 plaatjes robot_walk_0 t/m robot_walk_7
# die je daarvoor kunt gebruiken.
#
# Extra opdracht:
# Kijk of het lukt om het lopen aan / uit te zetten door op de robot te klikken.

class Robot(Actor):
    def __init__(self):
        super().__init__('robot_idle', (100,56))

robot = Robot()


def draw():
    screen.fill((255, 255, 255))
    robot.draw()

def update():
    pass


def on_mouse_down(pos, button):
    pass
