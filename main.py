import requests
import json
import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt 

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

if cosa == "nuovi casi" or "confirmed" or "deaths" or "recovered":
  try:
    print(df[cosa]) 
    plt.plot(df[cosa])
    plt.show()
  except KeyError:
    if cosa == "data":
      giorno = str(input("Insert here your day\n"))
      print(df[giorno : giorno])
    else:   
      if cosa == "da-a":
        giorno1 = str(input("Insert here your day\n"))
        giorno2 = str(input("Insert here your day\n"))
        x = (df[giorno1 : giorno2])
        print(x)
        plt.plot(x)
        plt.show()
      else:
        print("Niente input")  
else:
  print("Boh")     