from print_object import print_object

WIDTH = 512
HEIGHT = 256

# Opdracht: gedrag toevoegen
#
# De robot loopt nu wel, maar hij beweegt nog niet over het scherm.
# Kijk eens of je de robot willekeurig over het scherm kunt laten bewegen
# op het moment dat deze begint te lopen door deze bij iedere stap een
# beweging naar een willekeurige kant op te laten doen.
#
# Gebruik de random package voor het genereren van willekeurige getallen
#
# import random
#
# daarna kun je in de code random.randint(1, 5) gebruiken om bijvoorbeeld een
# willekeurig getal tussen de 1 en de 5 te krijgen.
#
# Extra opdracht:
# Kijk eens of je de X en Y optioneel mee kunt geven
#
# Extra opdracht:
# Probeer eens een tweede robot aan te maken
#
# Extra opdracht:
# Maak eens een class variable aan en gebruik die in je robot. Kijk eens wat er gebeurt als je die class variable aanpast of
# wat er gebeurt als je de instance variable aanpast.
#
#
# Doel van de opdracht:
# - Zien dat objecten zelfsturende elementen zijn en daar ook beslissingen kunnen maken onafhankelijk van elkaar.
# - Bij de extra opdracht zien wat variable scopes zijn.


class Robot(Actor):
    _IDLE_IMAGE = 'robot_idle'

    def __init__(self):
        self.is_lopende = False
        self.step = 0
        super().__init__(self.geef_plaatje())

    def geef_plaatje(self):
        if self.is_lopende:
            return 'robot_walk_' + str(self.step)
        return self._IDLE_IMAGE

    def neem_stap(self):
        self.step = self.step + 1
        if self.step > 7:
            self.step = 0
        # Als we lopende zijn, neem dan over 0.1 seconde weer een stap.
        # hierdoor creeren we een eigen loop loop los van de alemene programma loop
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
print_object(robot)


def draw():
    # Draw wordt iedere keer dat het scherm getekend moet worden aangeroepen. Eerst maken we het scherm leeg
    screen.fill((255, 255, 255))
    # En daarna vragen we aan de robot om zichzelf te tekenen op het scherm
    robot.draw()

def update():
    pass

def on_mouse_down(pos, button):
    # Als een muisknop ingerdukt wordt, en het is de linker muisknop EN de positie van de muis
    # botst met de robot wissel dan van lopen.
    if button == mouse.LEFT and robot.collidepoint(pos):
        robot.wissel_lopen()

