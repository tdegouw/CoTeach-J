class Monster:

    def __init__(self, naam: str):
        self.naam = naam
        print("Ik leef en heet " + self.naam)

    def __repr__(self):
        return "Ik heet {naam} en heb id {id}".format(naam=self.naam, id=id(self))
    def __del__(self):
        print("En nu is {} niet meer!".format(self.naam))


joep = Monster("Joep")
kees = Monster("Kees")
print(joep)
print(kees)
del(joep)
del(kees)