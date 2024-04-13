import gc


class Monster:

    def __init__(self, naam: str, kracht: int):
        self.naam = naam
        self.kracht = kracht
        self.superkracht = False

    def __str__(self):
        if self.superkracht:
            return 'super' + self.naam
        return self.naam

    def __eq__(self, other):
        return self.kracht == other.kracht

    def __lt__(self, other):
        if self.superkracht:
            return False
        return self.kracht < other.kracht


joep = Monster(naam="Joep", kracht=5)
henk = Monster(naam="Henk", kracht=6)

if henk > joep:
    print("Winnaar " + str(henk))
else:
    print("Winnaar " + str(joep))

joep.superkracht = True

if henk > joep:
    print("Winnaar " + str(henk))
else:
    print("Winnaar " + str(joep))

if henk.kracht > joep.kracht:
    print("Winnaar " + str(henk))
else:
    print("Winnaar " + str(joep))
