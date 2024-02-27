import asyncio
import time
import requests

class Persoon:
    def __init__(self, naam: str, bsn: str):
        self.naam = naam
        self.bsn = bsn


async def roep_api_aan(volgorde: int):
    print("Aanroep {}: gestart".format(volgorde))
    # optie 1: Maak de call naar requests.get
    resp = await asyncio.to_thread(requests.get, url="http://api.hastur.nl/gba.php")
    print("Aanroep {}: klaar".format(volgorde))
    return Persoon(resp.json().get('persoon').get('naam'), resp.json().get('persoon').get('bsn'))

async def main():
    start_tijd = time.time()
    personen = list()


    # tasks = [roep_api_aan(i) for i in range(10)]
    # resultaten = await asyncio.gather(*tasks)

    # tasks is een list van verwijzingen naar functies en de parameters
    # omdat gather de functies als argument mee wil hebben moeten we de de list
    # weer omzetten naar argumenten, daarvoor gebruiken we de unpacking (*) voor.

    # Dit is exact hetzelfde als de volgende code
    resultaten = await asyncio.gather(
        roep_api_aan(0),
        roep_api_aan(1),
        roep_api_aan(2),
        roep_api_aan(3),
        roep_api_aan(4),
        roep_api_aan(5),
        roep_api_aan(6),
        roep_api_aan(7),
        roep_api_aan(8),
        roep_api_aan(9),
    )
    # Nu gaan we door alle resultaten heen en voegen ze toe aan onze totale lijst.
    for resultaat in resultaten:
        personen.append(resultaat)
    totale_tijd = time.time() - start_tijd
    print("Totale duur {:.2f}".format(abs(totale_tijd)))

    for item in personen:
        print("{} : {}".format(item.bsn, item.naam))

asyncio.run(main())

