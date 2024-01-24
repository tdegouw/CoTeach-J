from epd import Epd


def laad_kamers(epd: Epd):
    print("Start met laden van de kamers")
    file = open("bestanden/kamerlijst.csv", "r")
    # Iedere regel is <kamernummer>,<Kamernaam>
    for line in file:
        kamernummer, naam = line.strip().split(',')
        print("** Bezig met inladen kamer {} - {}".format(kamernummer, naam))
        epd.maak_kamer(kamernummer=kamernummer, naam= naam)
    print("Kamers geladen: {}".format(epd.geef_kamertotaal()))

def laad_patienten(epd: Epd):
    print("Start met laden van de patienten")
    ## Laad je patienten in het ziekenhuis

    print("patienten geladen: {}".format(epd.geef_patiententotaal()))


def start_epd():
    mijn_epd = Epd(ziekenhuis='Mijn ziekenhuis')
    laad_kamers(epd=mijn_epd)
    laad_patienten(epd=mijn_epd)


if __name__ == "__main__":
    print("Start met laden van het EPD")
    start_epd()
