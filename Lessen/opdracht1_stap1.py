WIDTH = 512
HEIGHT = 256

male = Actor('male_idle')
female = Actor('female_idle')

male.pos = 100, 56
female.pos = 200, 56

class Character(Actor):

    def wissel_plaatje(self):
        if self.image == 'robot_idle':
            self.image = 'robot_think'
        else:
            self.image = 'robot_idle'


    def set_robot_think(self):
        self.image = 'robot_think'
        clock.schedule_unique(self.set_robot_idle, 1.0)

    def set_robot_idle(self):
        self.image = 'robot_idle'
        clock.schedule_unique(self.set_robot_think, 1.0)

robot = Character('robot_idle')
robot.pos = 300,56
robot.set_robot_think()

def draw():
    screen.fill((255, 255, 255))
    male.draw()
    female.draw()
    robot.draw()

def update():
    pass


def on_mouse_down(pos, button):
    pass
