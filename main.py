import requests
import json
import datetime
import numpy as np

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = "Italy"
cosa = "confirmed"

data = []
for righe in dati[nation]:
  strdata = datetime.datetime.strptime(righe['date'], "%Y-%m-%d")
  data.append(strdata.strftime("%d/%m/%Y"))

fir = [] 
for i in dati[nation]:
  fir.append(i[cosa])
   
sec = np.array([fir[0:-1]])
ter = np.array([fir[1:len(fir)]])
#fourth = np.array([ter])
data_np = np.array(data)

nuovi_casi = ter - sec
print(nuovi_casi)