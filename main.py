import requests
import json
import datetime 

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = "Italy"
da_strp = "01/02/2020"
a_strp = "29/02/2020"
da = datetime.datetime.strptime(da_strp, "%d/%m/%Y")
a = datetime.datetime.strptime(a_strp, "%d/%m/%Y")

data = []
days = []   
fir = []
for info in dati[nation]:
  fir.append(info["confirmed"])
  days.append(info["date"])
  strdata = datetime.datetime.strptime(info['date'], "%Y-%m-%d")
  data.append(strdata.strftime("%d/%m/%Y"))
  date_object = datetime.datetime.strptime(data, "%d/%m/%Y")
   
results = []   
for i in range(days[da], days[a]):
    results.append(i)
    print(results)

