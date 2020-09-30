import json
with open('V 4.0\ita.json', 'r') as ita: 
   dati = json.load(ita)

day = input("Insert here the date you want see the info e.g. 24/03/2020\n")

def _24_02(x):
   print(dati[0])
def _25_02(x):
   print(dati[1]) 
def _26_02(x):
   print(dati[2])   
default = "Unknown input"    
    
switch = {
   '24/02/2020' : _24_02,
   '25/02/2020' : _25_02,
   '26/02/2020' : _26_02,
} 
try:
   switch[day](day)
except:
   print(default)   

