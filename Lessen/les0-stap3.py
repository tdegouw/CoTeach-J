WIDTH = 1024
HEIGHT = 768

male = Actor('male_idle')
female = Actor('female_idle')

male.pos = 100, 56
female.pos = 200, 56

class Character(Actor):

    def __init__(self, character_type: str, x: int, y: int):
        self.character_type = character_type
        self.moving = False
        super().__init__(self.geef_plaatje())
        self.step = 0
        self.x = x
        self.y = y

    def geef_plaatje(self):
        if self.moving:
            return self.character_type + '_walk_' + str(self.step)
        return self.character_type + '_idle'

    def neem_stap(self):
        self.step = self.step + 1
        if self.step > 7:
            self.step = 0
        # Zijn we nog aan het lopen? Neem dan over een seconde nog een stap
        if self.moving:
            clock.schedule_unique(self.neem_stap, 0.1)

    def wissel_lopen(self):
        self.moving = not self.moving
        if self.moving:
            self.neem_stap()


    def draw(self):
        self.image = self.geef_plaatje()
        super().draw()

robot = Character('robot', 300, 56)


def draw():
    screen.fill((255, 255, 255))
    male.draw()
    female.draw()
    robot.draw()

def update():
    pass

def on_mouse_down(pos, button):
    global score
    if button == mouse.LEFT and robot.collidepoint(pos):
        robot.wissel_lopen()

