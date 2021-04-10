import requests
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nation = str(input("Insert here a nation\n"))

if nation == "Italy":
    url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json'
    reponse = requests.get(url)
    dati = json.loads(reponse.content)

    conf, tamp, mor, n_pos = [], [], [], []
    for i in dati:
      conf.append(i["totale_casi"])
      tamp.append(i["tamponi"])
      mor.append(i["deceduti"])
      n_pos.append(i["nuovi_positivi"])

    del conf[-1]
    del n_pos[-1]
    nuovi_morti = np.array([mor])
    del mor[-1]
    n_m = np.diff(nuovi_morti)
    nuovi_m = n_m.reshape(len(conf), 1)

    nuovi_tamponi = np.array([tamp])
    del tamp[-1]
    n_t = np.diff(nuovi_tamponi)
    nuovi_t= n_t.reshape(len(conf), 1)

    dates = pd.date_range('20200224', periods = len(mor))
    df = pd.DataFrame(index=dates)
    df['tamponi tot'] = tamp
    df['casi tot'] = conf
    df['morti tot'] = mor
    df['nuovi positivi'] = n_pos
    df['nuovi morti'] = nuovi_m
    df['nuovi tamponi'] = nuovi_t

    print(df)

else:
   print("Write one of those options: \nConfirmed, deaths, recovered, nuovi casi, nuovi morti, nuovi ricoverati, data, da-a")
   cosa = str(input("Insert here what do you want receive\n"))

   url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
   reponse = requests.get(url)
   dati = json.loads(reponse.content)

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
            print("year-month-day")
            giorno = str(input("Insert here your day\n"))
            print(df[giorno : giorno])
        else:
            if cosa == "da-a":
                print("year-month-day")
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
