import json
with open('V 4.0\ita.json', 'r') as ita: 
   data = json.load(ita)
print(data[0])