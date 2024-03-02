from print_object import print_object
import time

WIDTH = 512
HEIGHT = 256

# Link naar de documentatie:
# - https://pygame-zero.readthedocs.io/en/stable/
#
# Link naar de mu editor:
# - https://codewith.mu/
#
# Als je Thonny gebruikt moet je eerst de PGZero module installeren
# - tools -> manage packages -> zoek naar PGZero
#
# En daarna PGZero modus aanzetten
# - Run -> PyGame Zero Mode
#
#
# Start met het downloaden van de hele repository, anders mis je de plaatjes.
#
# Opdracht: Kijk of het je lukt om door overerving de robot zelf te plaatsen zonder
# dat je parameters hoeft mee te geven. Dus zorg dat je in onderstaand programma
# de class Robot gaat gebruiken en niet langer de Actor class.
#
# Tips:
# de constructor van de class is:
#   def __init__(self):
#
# om de constructor van de parent aan te roepen gebruik je
#  super().__init__(...)
#
# print_object kun je gebruiken om meer te weten te komen over een object.
#
# Handleiding: https://pygame-zero.readthedocs.io/en/stable/builtins.html#actors
#
# Doel van de opdracht:
# - Begrijpen hoe objecten gedrag en data samenbrengen en een eigen state hebben
# - Zien hoe een constructor werkt
# - Zien wat pointers zijn

class Robot(Actor):
    pass


# Een actor aanmaken volgens de handleiding van PyGame Zero
robot = Actor('robot_idle')
robot.pos = 100, 56
# Om de verwijzing te zien
print("Onze robot bij het aanmaken id {}".format(id(robot)))


# Om te zien hoe het object er in het geheugen uitziet
#print_object(robot, True, True, False)


def draw():
    # Draw wordt iedere keer dat het scherm getekend moet worden aangeroepen. Eerst maken we het scherm leeg
    screen.fill((255, 255, 255))
    # En daarna vragen we aan de robot om zichzelf te tekenen op het scherm
    robot.draw()

def update():
    # Update wordt iedere keer dat het scherm weergegeven wordt aangeroepen
    pass

def on_mouse_down(pos, button):
    # Als iemand de muis klikt in het scherm wordt deze functie async aangeroepen met de button die geklikt is en de positie
    # waar geklikt is in het scherm. (X, Y)

    # We gaan nu opnieuw de global robot variable opnieuw aanmaken
    global robot
    # Probeer het eens zonder global: Waarom gebeurt er nu iets anders?
    robot = Actor('robot_idle')
    robot.pos = 400, 56
    print("Onze robot heeft nu id {}".format(id(robot)))

