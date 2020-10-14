import requests
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

nuovi_casi = [0]  
while len(fir) > 0:
  x = fir[0]
  z = sec[0] - x
  nuovi_casi.append(z)
  del fir[0]
  del sec[0]
  if len(fir) == 1:
    break


for cat in enumerate(nuovi_casi, 1):
  print(cat)
