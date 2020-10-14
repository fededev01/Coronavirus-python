import requests
import json
import numpy as np

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = "Italy"
   
fir = []
for info in dati[nation]:
  fir.append(info["confirmed"])  

sec = np.array(fir)

nuovi = np.array([0]) 
list = []
 
while len(fir) > 0:
  z = sec[1] - sec[0]
  list.append(z)
  np.delete(sec, [0])
  del fir [0]
  for cat in enumerate(list, 1):
    print(cat)

