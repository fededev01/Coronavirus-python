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

nuovi = np.array([0]) 
list = [0]
 
while len(fir) > 0:
  z = fir[1] - fir[0]
  list.append(z)
  np.delete(fir, [0])
  del fir [0]
  if len(fir) == 1:
    break


for cat in enumerate(list, 1):
  print(cat)


