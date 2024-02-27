import asyncio
import time
import requests


# Je hebt als het goed is de code nu asynchroon gemaakt, maar je hebt nog niet aangegeven dat je de
# code gelijktijdig wil uitvoeren want de code wordt nog steeds in een loop aangeroepen.
# Om code als coroutines asynchroon uit te voeren moeten we gebruik maken van asyncio voor het starten van taken.
#
# Probeer door middel van asyncio.gather, of asyncio.TaskGroup 10 keer de API aan te roepen.
#
# tip:
#
# https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently
# https://docs.python.org/3/library/asyncio-task.html#task-groups
#
class Persoon:
    def __init__(self, naam: str, bsn: str):
        self.naam = naam
        self.bsn = bsn


async def roep_api_aan(volgorde: int):
    print("API wordt aangeroepen volgorde: {}".format(volgorde))
    resp = requests.get(url="http://api.hastur.nl/gba.php")
    return Persoon(resp.json().get('persoon').get('naam'), resp.json().get('persoon').get('bsn'))


async def main():
    start_tijd = time.time()
    personen = list()
    for i in range(0, 10):
        personen.append(await roep_api_aan(i))
    totale_tijd = time.time() - start_tijd
    print("Totale duur {:.2f}".format(abs(totale_tijd)))

    for item in personen:
        print(item.naam + "\n")


asyncio.run(main())
