import requests
import json

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = str(input("Insert here a nation"))
cosa = str(input("Insert here what do you want receive"))

fir = []
for info in dati[nation]:
  fir.append(info[cosa])

print(fir)
