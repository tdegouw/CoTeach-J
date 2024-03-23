from print_object import print_object
import time
import pgzrun

WIDTH = 512
HEIGHT = 256

# Link naar de documentatie:
# - https://pygame-zero.readthedocs.io/en/stable/
#
# Link naar de mu editor:
# - https://codewith.mu/
#
# Als je Thonny gebruikt moet je eerst de PGZero module installeren
# - tools → manage packages → zoek naar PGZero
#
# En daarna PGZero modus aanzetten
# - Run → PyGame Zero Mode
#
#
# Start met het downloaden van de hele repository, anders mis je de plaatjes.
#
# Opdracht:
# - Kijk of je een object van het type 'Actor' aan kunt maken met de kennis die je nu hebt
# - gebruik een van de plaatjes in de 'images' folder, je hoeft alleen de bestandsnaam te geven zonder .jpg
#
# Vervolgopdracht:
#
# - Kijk of je de X en Y positie van de actor ook kunt zetten
#
# print_object kun je gebruiken om meer te weten te komen over een object.
#
# Handleiding: https://pygame-zero.readthedocs.io/en/stable/builtins.html#actors
#
# Doel van de opdracht:
# - De eerste verkenning met objecten, ze aanmaken en de state manipuleren
#
# TODO: Typ hieronder je code

# Om te zien hoe het object er in het geheugen uitziet
#print_object(mijn_object, True, True, False)

def draw():
    # Draw wordt iedere keer dat het scherm getekend moet worden aangeroepen. Eerst maken we het scherm leeg
    screen.fill((255, 255, 255))
    # TODO: Hier moet je nog je nieuwe object zichzelf laten tekenen door de .draw method aan te roepen.


def update():
    # Update wordt iedere keer dat het scherm weergegeven wordt aangeroepen
    pass

def on_mouse_down(pos, button):
    # Als iemand de muis klikt in het scherm wordt deze functie async aangeroepen met de button die geklikt is en de positie
    # waar geklikt is in het scherm. (X, Y)
    pass