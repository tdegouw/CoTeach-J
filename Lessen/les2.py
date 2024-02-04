from modules.les1.epd import Epd
from modules.les2.epd_gui import EpdGui
from modules.les1.bestandslader import Bestandslader


def laad_kamers(epd: Epd):
    print("Start met laden van de kamers")
    lader = Bestandslader('kamerlijst.csv')
    regel = lader.geef_regel()
    while regel is not None:
        print(regel)
        epd.maak_kamer(kamernummer=regel['ID'], naam=regel['naam'])
        regel = lader.geef_regel()

    print("Kamers geladen: {}".format(epd.geef_kamertotaal()))

def laad_patienten(epd: Epd):
    print("Start met laden van de patienten")
    ## Laad je patienten in het ziekenhuis

    print("patienten geladen: {}".format(epd.geef_patiententotaal()))


def start_epd():
    mijn_epd = EpdGui(ziekenhuis='Mijn ziekenhuis')
    laad_kamers(epd=mijn_epd)
    laad_patienten(epd=mijn_epd)
    mijn_epd.draw()


if __name__ == "__main__":
    print("Start met laden van het EPD")
    start_epd()
