import requests
import json
import datetime
import numpy as  np

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = str(input("Insert here a nation\n"))
cosa = str(input("Insert here what do you want receive\n"))
conf = "confirmed"

resp = dati[nation]
data = []
for righe in dati[nation]:
  strdata = datetime.datetime.strptime(righe['date'], "%Y-%m-%d")
  data.append(strdata.strftime("%d/%m/%Y"))

fir = [] 
for i in dati[nation]:
  fir.append(i[conf]) 
sec = np.array([fir[0:-1]])
ter = np.array([fir[1:len(fir)]])
nuovi_casi = ter - sec 

if cosa == "nuovi casi":
  print(nuovi_casi)
elif cosa == "confirmed" or "deaths" or "recovered":
  for info in dati[nation]:
    data = datetime.datetime.strptime(info['date'], "%Y-%m-%d")
    strdata = data.strftime("%d/%m/%Y")
    print(strdata, info[cosa])
else:
  print("Input sconosciuto")  
