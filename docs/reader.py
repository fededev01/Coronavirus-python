from pip._vendor import requests
import json


url = 'https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json'
reponse = requests.get(url)
dati = json.loads(reponse.content)


day = input("Insert here the date you want see the info e.g. 24/03/2020\n")
nation = str(input("Insert here your nation\n"))