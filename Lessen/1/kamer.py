class Kamer(object):
    __kamernummer: str
    naam: str

    def __init__(self, kamernummer: str, naam: str):
        self.__kamernummer = kamernummer
        self.naam = naam

    @property
    def nummer(self):
        return self.__kamernummer


