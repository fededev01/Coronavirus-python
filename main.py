import requests
import json
import numpy as  np
import pandas as pd

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = str(input("Insert here a nation\n"))
cosa = str(input("Insert here what do you want receive\n"))

conf = [] 
rec = []
mor = []
for i in dati[nation]:
  conf.append(i["confirmed"])
  rec.append(i["recovered"])
  mor.append(i["deaths"])  

sec = np.array([conf])
ter = conf[1: len(conf)]
ter.append(conf[-1])
quar = np.array([ter])
nuovi_casi = ter - sec

nuovi = nuovi_casi.reshape(len(mor), 1)
dates = pd.date_range('20200122', periods = len(rec))
df = pd.DataFrame(index = dates)
df['recovered'] = rec
df['confirmed'] = conf
df['deaths'] = mor
df['nuovi casi'] = nuovi

if cosa == "nuovi casi":
  print(df['nuovi casi'])
elif cosa == "confirmed":
  print(df['confirmed'])
elif cosa == "deaths":
  print(df['deaths'])
elif cosa == "recovered":
  print(df['recovered']) 
else:
  print("Boh")     