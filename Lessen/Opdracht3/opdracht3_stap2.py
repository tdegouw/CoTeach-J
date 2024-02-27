import time

import requests

# Sequentieel aanroepen van de API is langzaam. Maar dat gaan we versnellen
#
#
# Opdracht:
#
# - Probeer de API aanroep nu als een coroutine te scrijven en deze aan te roepen met
# await.
# - Maak de main routine ook een async methode
# - run je programma door 'asyncio.run(main())' aan te roepen
#
# https://docs.python.org/3/library/asyncio-task.html
#
# Tips:
# - import asyncio bovenaan je programma
# - maak de functie "async"
# - gebruik "await" om de functie aan te roepen

class Persoon:
    def __init__(self, naam: str, bsn: str):
        self.naam = naam
        self.bsn = bsn


start_tijd = time.time()
personen = list()

for i in range(0, 10):
    resp = requests.get(url="http://api.hastur.nl/gba.php")
    personen.append(Persoon(resp.json().get('persoon').get('naam'), resp.json().get('persoon').get('bsn')))

totale_tijd = time.time() - start_tijd
print("Totale duur {:.2f}".format(abs(totale_tijd)))


for item in personen:
    print(item.naam + "\n")

