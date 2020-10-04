from pip._vendor import requests
import json

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = "Italy"

date = []   
fir = []
for info in dati[nation]:
  fir.append(info["confirmed"])
  date.append(info["date"])
    
lung = len(fir)  
sec = []
for itemA in fir[1:lung]:
  sec.append(itemA)

nuovi_casi = []  