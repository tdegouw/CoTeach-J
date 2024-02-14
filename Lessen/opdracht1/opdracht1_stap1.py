from print_object import print_object

WIDTH = 512
HEIGHT = 256

# Opdracht: Overerven en state aanpassen
#
# Kijk of het lukt om het plaatje te laten wisselen
# om de robot te laten lopen. Er zijn 7 plaatjes robot_walk_0 t/m robot_walk_7
# die je daarvoor kunt gebruiken.
#
# Extra opdracht:
#
# Kijk of het je lukt het lopen te roteren, dus van 7 weer te beginnen bij 0
#
# Extra opdracht:
#
# Kijk of het je lukt de rotatie te starten en stoppen door een method aan te maken
# om het lopen aan of uit te zetten
#
# Extra opdracht:
#
# Kijk of het lukt om het lopen aan / uit te zetten door op de robot te klikken.
#
# Leestip: https://pygame-zero.readthedocs.io/en/stable/hooks.html#event-handling-hooks
# en zoek eens op 'collidepoint' in de documentatie.
#
# Doel van de opdracht: Begrijpen hoe je de state van objecten manipuleert

class Robot(Actor):
    def __init__(self):
        super().__init__('robot_idle', (100,56))

robot = Robot()
print_object(robot)

def draw():
    screen.fill((255, 255, 255))
    robot.draw()

def update():
    pass


def on_mouse_down(pos, button):
    pass
