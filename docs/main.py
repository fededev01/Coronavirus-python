from pip._vendor import requests
import json
import datetime
from datetime import timedelta


url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)


data = "2020/01/22"
nation = "Italy"

data_2 = data + timedelta(days = 1)

nuovi_casi = []

for righe in dati[nation]:
   x = dati[data]["confirmed"]
   y = dati[data_2]["confirmed"]
   z = y - x
   nuovi_casi.append(z)
