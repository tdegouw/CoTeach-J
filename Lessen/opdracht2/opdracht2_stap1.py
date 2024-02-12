from modules.epd import Epd
from modules.bestandslader import Bestandslader

# Opdracht:
#
# We willen graag kunnen zoeken met functionele queries. Hiervoor is in het EPD
# een zoek_patienten stub opgenomen.
#
# Maak een pure functie die een functie (of Labda) accepteert en alle nederlandse patienten laat zien


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
    lader = Bestandslader('patienten.csv')
    regel = lader.geef_regel()
    ## Laad je patienten in het ziekenhuis
    while regel is not None:
        print(regel)
        print(epd.geef_kamer(regel['locatie']))
        regel = lader.geef_regel()

    print("patienten geladen: {}".format(epd.geef_patiententotaal()))


def start_epd():
    mijn_epd = Epd(ziekenhuis='Mijn ziekenhuis')
    laad_kamers(epd=mijn_epd)
    laad_patienten(epd=mijn_epd)


if __name__ == "__main__":
    print("Start met laden van het EPD")
    start_epd()
