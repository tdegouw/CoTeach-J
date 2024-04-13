class Driehoek:
    def __init__(self, a: int, b:int):
        self.a = a
        self.b = b

    def geef_c(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5

    def geef_omtrek(self):
        return (self.a + self.b + self.geef_c())


c = Driehoek(5, 10)
print("Uitkomst: " + str(c.geef_c()))
print("Omtrek: " + str(c.geef_omtrek()))