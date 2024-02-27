from modules.epd import Epd
from modules.kamer import Kamer
from modules.bestandslader import Bestandslader


def laad_kamers(epd: Epd):
    print("Start met laden van de kamers")
    lader = Bestandslader('kamerlijst.csv')
    regel = lader.geef_regel()
    while regel is not None:
        print(regel)
        epd.maak_kamer(kamernummer=regel['ID'], naam=regel['naam'], afdeling=regel['afdeling'])
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


def check_afdeling(kamer):
    return kamer.afdeling == 'Emoji_Overdosis_Eenheid'


def log_aanroep(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} aangeroepen met argumenten: {args}, {kwargs}")
        return func(*args, **kwargs)

    return wrapper


def zoek_kamers(epd: Epd):
    # Kamers met een named functie
    print("Kamers in: Emoji_Overdosis_Eenheid")
    for item in epd.zoek_kamers(check_afdeling):
        print(item.naam)


@log_aanroep
def zoek_kamers2(epd: Epd):
    # Kamers met een anonieme functie / lambda functie
    print("Kamers in: Emoji_Overdosis_Eenheid")
    for item in epd.zoek_kamers(lambda x: x.afdeling == 'Emoji_Overdosis_Eenheid'):
        print(item.naam)


def start_epd():
    mijn_epd = Epd(ziekenhuis='Mijn ziekenhuis')
    laad_kamers(epd=mijn_epd)
    laad_patienten(epd=mijn_epd)
    zoek_kamers(epd=mijn_epd)
    zoek_kamers2(epd=mijn_epd)


if __name__ == "__main__":
    print("Start met laden van het EPD")
    start_epd()
