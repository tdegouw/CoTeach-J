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
# Doel van de opdracht:
# - Begrijpen hoe je de state van objecten manipuleert


class Robot(Actor):
    _IDLE_IMAGE = 'robot_idle'
    
    def __init__(self):
        # Omdat we de constructor overloaden moeten we de parent constructor ook aanroepen.
        super().__init__(self._IDLE_IMAGE, (100,56))
        
# We maken een nieuwe variabele 'robot' en maken dit een Robot (nieuwe instantie van de Robot class)
robot = Robot()

# Daarna kijken we hoe deze er uit ziet
print_object(robot)

def draw():
    # Draw wordt iedere keer dat het scherm getekend moet worden aangeroepen. Eerst maken we het scherm leeg
    screen.fill((255, 255, 255))
    # En daarna vragen we aan de robot om zichzelf te tekenen op het scherm
    robot.draw()

def update():
    pass


def on_mouse_down(pos, button):
    pass
