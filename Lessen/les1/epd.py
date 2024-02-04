from .kamer import Kamer


class Epd(object):

    def __init__(self, ziekenhuis: str):
        self.ziekenhuis = ziekenhuis
        self.kamers = dict()

    def maak_kamer(self, kamernummer: str, naam: str):
        self.kamers[kamernummer] = Kamer(kamernummer=kamernummer, naam=naam)

    def maak_patient(self, patientnaam):
        # Vul deze zelf in
        pass

    def geef_kamertotaal(self):
        return len(self.kamers)

    def geef_patiententotaal(self):
        pass
