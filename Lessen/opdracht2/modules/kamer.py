class Kamer(object):

    def __init__(self, kamernummer: str, naam: str, afdeling: str):
        self.__kamernummer = kamernummer
        self.naam = naam
        self.afdeling = afdeling

    @property
    def nummer(self):
        return self.__kamernummer


