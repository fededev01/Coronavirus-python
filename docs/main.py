from pip._vendor import requests
import json
import datetime
from datetime import timedelta
#import numpy as np


url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)


nation = "Italy"

nuovi_casi = [0]
dictlist = []

for righe in dati[nation]:
   
   x = righe
   y = next(righe+1)
   z = y - z
   nuovi_casi.append(z)
   print(z)