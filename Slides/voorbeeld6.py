import gc

class Monster:

    def __init__(self, naam: str):
        self.naam = naam
        print("Ik leef en heet " + self.naam)

    def __repr__(self):
        return "Ik heet {naam} en heb id {id}".format(naam=self.naam, id=id(self))
    def __del__(self):
        print("En nu is {} niet meer!".format(self.naam))

def print_objects():
    for obj in gc.get_objects():
        if isinstance(obj, Monster):
            print(obj)

joep = Monster("Joep")
print_objects()
kees = Monster("Kees")
print_objects()
del(kees)
print_objects()
del(joep)
print_objects()
