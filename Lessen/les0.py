WIDTH = 1024
HEIGHT = 768

class Character(Actor):
    pass



male = Actor('male_idle')
female = Actor('female_idle')
male.pos = 100, 56
female.pos = 200, 56

robot = Character('robot_idle')
robot.pos = 300, 56

def draw():
    screen.fill((255, 255, 255))
    male.draw()
    female.draw()
    robot.draw()

def update():
    pass
