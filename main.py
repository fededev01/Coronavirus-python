import requests
import json
import datetime

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = str(input("Insert here a nation\n"))
cosa = str(input("Insert here what do you want receive\n"))

resp = dati[nation]
data = []
for righe in dati[nation]:
    strdata = datetime.datetime.strptime(righe['date'], "%Y-%m-%d")
    data.append(strdata.strftime("%d/%m/%Y"))

if cosa == "nuovi casi":
  fir = []
  for y in dati[nation]:
    fir.append(y["confirmed"])
  nuovi_casi = [0]  
  while len(fir) > 0:
    x = fir[0]
    z = fir[1] - x
    nuovi_casi.append(z)
    del fir[0]
    if len(fir) == 1:
      break
  while len(nuovi_casi) > 0:
        print(data[0], nuovi_casi[0])
        del data[0]
        del nuovi_casi[0]
        if len(nuovi_casi) == 0:
          break
elif cosa == "confirmed" or "deaths" or "recovered":
  for info in dati[nation]:
    data = datetime.datetime.strptime(info['date'], "%Y-%m-%d")
    strdata = data.strftime("%d/%m/%Y")
    print(strdata, info[cosa])
else:
  print("idk")  
