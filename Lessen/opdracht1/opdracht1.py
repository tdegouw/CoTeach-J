from print_object import print_object

WIDTH = 512
HEIGHT = 256

# https://pygame-zero.readthedocs.io/en/stable/
#
# Opdracht: Kijk of het je lukt om door overerving de robot zelf te plaatsen zonder
# dat je parameters hoeft mee te geven. Dus zorg dat je in onderstaand programma
# de class Robot gaat gebruiken
#
# Tips:
# de constructor van de class is:
#   def __init__(self):
# om de constructor van de parent aan te roepen gebruik je
#  super().__init__(...)
#
# print_object kun je gebruiken om meer te weten te komen over een object.
#
# Handleiding: https://pygame-zero.readthedocs.io/en/stable/builtins.html#actors
#
# Doel van de opdracht: Begrijpen hoe objecten gedrag en data samenbrengen en een eigen state hebben
#

class Robot(Actor):
    pass


robot = Actor('robot_idle')
robot.pos = 100, 56
print_object(robot, True, True, False)


def draw():
    # Draw wordt iedere keer dat het scherm getekend moet worden aangeroepen
    screen.fill((255, 255, 255))
    robot.draw()

def update():
    # Update wordt iedere keer dat het scherm weergegeven wordt aangeroepen
    pass

def on_mouse_down(pos, button):
    pass
