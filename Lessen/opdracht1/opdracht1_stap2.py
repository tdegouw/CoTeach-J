from print_object import print_object

WIDTH = 512
HEIGHT = 256

# Opdracht: attributen manipuleren
#
# Je ziet dat de robot hard rent als je iedere update een
# stap zet. Probeer het eens door gebruik te maken van asynchroniteit
# in de code, in dit geval door gebruik te maken van de clock / scheduler
#
# https://pygame-zero.readthedocs.io/en/stable/builtins.html#clock
#
# Doel van de opdracht:
#
# Begrijpen dat er naast de standaard loop en method calls
# ook andere mogelijkheden zijn om de program flow aan te passen. (Asynchroniteit)
# Een inkijkje in method overloading

class Robot(Actor):
    _IDLE_IMAGE = 'robot_idle'

    def __init__(self):
        self.is_lopende = False
        self.step = 0
        super().__init__(self.geef_plaatje(), (100, 56))

    def geef_plaatje(self):
        # Deze method geeft iedere keer dat deze aangeroepen wordt de naam van het volgende plaatje in de loopvolgorde
        # wanneer de robot lopende is. Als de robot niet lopende is dan wordt de naam van het idle plaatje terug gegeven
        if self.is_lopende:
            self.step = self.step + 1
            if self.step > 7:
                self.step = 0
            return 'robot_walk_' + str(self.step)
        return self._IDLE_IMAGE

    def wissel_lopen(self):
        self.is_lopende = not self.is_lopende

    def draw(self):
        # We 'Overloaden' de 'draw' method, hierdoor kunnen we iets doen voordat de actor getekend wordt
        # We vervangen snel het plaatje voordat de actor getekend wordt.
        self.image = self.geef_plaatje()
        # Maar we moeten niet vergeten de 'draw' method van de parent aan te roepen.
        super().draw()

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
    if button == mouse.LEFT and robot.collidepoint(pos):
        robot.wissel_lopen()
