from modules.les2.les1 import start_epd

WIDTH = 1024
HEIGHT = 768

bed = Rect((150, 400), (20, 20))

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    bed = Actor('character/face/completes/face1')
    bed.pos = 100, 56
    bed.draw()

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Eek!")
    else:
        print("You missed me!")

def update():
    pass


epd = start_epd()
