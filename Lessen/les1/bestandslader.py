import os


class Bestandslader:

    def __init__(self, bestandsnaam: str):
        file = self.__laad_bestand(bestandsnaam)
        self.regels = list()
        self.index = 0
        sleutels = list()
        self.regels = list()
        regel_teller = 0
        for line in file:
            regel_teller = regel_teller + 1
            if regel_teller == 1:
                sleutels = line.strip().split(',')
            else:
                self.regels.append(dict(zip(sleutels, line.strip().split(','))))

    def __laad_bestand(self, bestandsnaam):
        for prefix in ['', 'bestanden/', '../bestanden/']:
            try:
                print("Opent: " + prefix + bestandsnaam + ' Vanuit ' + os.getcwd())
                return open(prefix + bestandsnaam, "r")
            except FileNotFoundError:
                pass

        raise FileNotFoundError('Kan bestand niet vinden: ' + bestandsnaam)

    def aantal_regels(self):
        # Geef het aantal regels uit het bestand
        return len(self.regels)

    def geef_regel(self):
        # Geef een regel uit het bestand
        if self.index < len(self.regels):
            item = self.regels[self.index]
            self.index += 1
            return item
        else:
            return None

    def reset(self):
        # Begin het bestand weer van voren af aan te lezen
        self.index = 0
