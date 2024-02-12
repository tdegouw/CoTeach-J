from .kamer import Kamer
from .patient import Patient

class Epd(object):

    def __init__(self, ziekenhuis: str):
        self.ziekenhuis = ziekenhuis
        self.kamers = dict()
        self.patienten = dict()

    def maak_kamer(self, kamernummer: str, naam: str, afdeling: str):
        self.kamers[kamernummer] = Kamer(kamernummer=kamernummer, naam=naam, afdeling=afdeling)

    def maak_patient(self, naam:str, adres:str, postcode, woonplaats:str, land:str, kamer:str):
        self.patienten.append(Patient(naam))

    def geef_kamertotaal(self):
        return len(self.kamers)

    def geef_kamer(self, code: str):
        return self.kamers.get(code)

    def zoek_patienten(self, func):
        # vul mij
        pass

    def geef_patiententotaal(self):
        pass

    def zoek_kamers(self, func):
        return list(filter(func, self.kamers.values()))
