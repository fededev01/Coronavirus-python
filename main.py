import requests
import json
import datetime 
import pandas as pd

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = "Italy"
da = "01/02/2020"
a = "29/02/2020"

days = []   
fir = []
oth = []
for info in dati[nation]:
  fir.append(info["confirmed"])
  days.append(info["date"])
  oth.append(info)
  strdata = datetime.datetime.strptime(info['date'], "%Y-%m-%d")
  data = (strdata.strftime("%d/%m/%Y"))
  date_object = datetime.datetime.strptime(data, "%d/%m/%Y")
   
results = []   
for i in range(fir[da:a]):
    results.append(i)
    print(results)