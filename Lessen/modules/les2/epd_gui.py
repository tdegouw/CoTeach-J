from ..les1.epd import Epd

WIDTH = 800
HEIGHT = 600
class EpdGui(Epd):

    def draw(self):
        screen.fill((128, 0, 0))