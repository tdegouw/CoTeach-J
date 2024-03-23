class Transportmiddel:
    AFSCHRIJFTERMIJN = 5

    def __init__(self, aanschafprijs: int, leeftijd: int):
        self.aanschafprijs = aanschafprijs
        self.leeftijd = leeftijd

    def waarde(self):
        if self.leeftijd >= self.AFSCHRIJFTERMIJN:
            return 0
        return self.aanschafprijs - ((self.aanschafprijs / self.AFSCHRIJFTERMIJN) * self.leeftijd)


class Auto(Transportmiddel):
    def __init__(self, aanschafprijs: int, leeftijd: int, kleur: str):
        self.kleur = kleur
        super().__init__(aanschafprijs, leeftijd)


auto1 = Auto(50000, 3, 'Rood')
print("Restwaarde: {restwaarde:.2f}".format(restwaarde=auto1.waarde()))
