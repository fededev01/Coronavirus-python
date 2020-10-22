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

#cambiare nome variabili
sec = np.array([conf])
ter = conf[1: len(conf)]
ter.append(conf[-1])
quar = np.array([ter]) #modificare 
nuovi_casi = ter - sec #sostituire ter con quar

cinq = np.array([mor])
sei = mor[1: len(mor)]
sei.append(mor[-1])
set = np.array([sei])
nuovi_morti = set - cinq

otto = np.array([rec])
nove = rec[1: len(rec)]
nove.append(rec[-1])
dieci = np.array([nove])
nuovi_ricoverati = dieci - otto
#fine variabili da cambiare

nuovi_c = nuovi_casi.reshape(len(mor), 1)
nuovi_m = nuovi_morti.reshape(len(mor), 1)
nuovi_r = nuovi_ricoverati.reshape(len(mor), 1)

dates = pd.date_range('20200122', periods = len(rec))
df = pd.DataFrame(index = dates)
df['recovered'] = rec
df['confirmed'] = conf
df['deaths'] = mor
df['nuovi casi'] = nuovi_c
df['nuovi morti'] = nuovi_m
df['nuovi dimessi'] = nuovi_r

if cosa == "nuovi casi" or "confirmed" or "deaths" or "recovered" or "nuovi morti" or "nuovi dimessi":
  try:
    print(df[cosa]) 
    plt.plot(df[cosa])
    plt.show()
    if cosa == "nuovi casi":
      n = np.sum(nuovi_c)
      print("La media di nuovi casi è: " + n / len(conf))
    elif cosa == "nuovi morti":
      n = sum(nuovi_m)
      print("La media di nuovi morti è: " + n / len(conf))
    elif cosa == "nuovi dimessi":
      n = sum(nuovi_r)
      print("La media di nuovi dimessi è: " + n / len(conf))
    else:
      pass    
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