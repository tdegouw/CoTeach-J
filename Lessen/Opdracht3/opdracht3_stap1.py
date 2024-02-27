from pprint import pprint

import requests

# Opdracht:
#
# Probeer nu een lijstje met 10 personen te vullen door 10x die api aan te roepen
#

class Persoon:
    def __init__(self, naam: str, bsn: str):
        self.naam = naam
        self.bsn = bsn


resp = requests.get(url='http://api.hastur.nl/gba.php')
ob = Persoon(resp.json().get('persoon').get('naam'), resp.json().get('persoon').get('bsn'))
pprint(vars(ob))