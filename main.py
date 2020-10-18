import requests
import json
import numpy as np
import pandas as pd

url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)

nation = "Italy"
da = "2020/02/01"
a = "2020/02/29"

one = []  
two = []
tre = []
for info in dati[nation]:
  one.append(info["recovered"])
  two.append(info["confirmed"])
  tre.append(info["deaths"])


dates = pd.date_range('22012020', periods = len(two))

df = pd.DataFrame(index = dates)
df['recovered'] = one
df['confirmed'] = two
df['deaths'] = tre
resp = df[da : a]
print(resp)



