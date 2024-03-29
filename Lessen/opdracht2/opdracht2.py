from modules.epd import Epd
from modules.bestandslader import Bestandslader

# Opdracht:
#
# Kijk of je de class voor de patient kunt maken
# en of je de gegevens uit de patienten set kunt inlezen in een nieuw te maken class genaamd patient


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
        regel = lader.geef_regel()

    print("patienten geladen: {}".format(epd.geef_patiententotaal()))


def start_epd():
    mijn_epd = Epd(ziekenhuis='Mijn ziekenhuis')
    laad_kamers(epd=mijn_epd)
    laad_patienten(epd=mijn_epd)


if __name__ == "__main__":
    print("Start met laden van het EPD")
    start_epd()
