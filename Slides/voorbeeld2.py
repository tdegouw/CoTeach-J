a = 5
b = 10
c = 0
def pythagoras():
    global a, b, c
    c = (a ** 2 + b ** 2) ** 0.5

pythagoras()
print("Uitkomst: " + str(c))