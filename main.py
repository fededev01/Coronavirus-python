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
variables = True 
while variables == True:
  if len(fir) > 0:
    for n in fir:
      z = sec[1] - sec[0]
      list.append(z)
      np.delete(sec, [0])
  else:    
    variables = False


list_arr = np.array(list)
nuovi_casi = np.concatenate((nuovi, list_arr))


for cat in enumerate(nuovi_casi, 1):
  print(cat)