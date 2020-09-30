import json
with open('V 4.0\ita.json', 'r') as ita: 
   dati = json.load(ita)



def _24_02(x):
   print(dati[0])
def _25_02(x):
   print(dati[1]) 
def _26_02(x):
   print(dati[2]) 
def _27_02(x):
   print(dati[3])
def _28_02(x):
   print(dati[4]) 
def _29_02(x):
   print(dati[5])        
default = "Unknown input"    
    
Italia = {
   '24/02/2020' : _24_02,
   '25/02/2020' : _25_02,
   '26/02/2020' : _26_02,
   '27/02/2020' : _27_02,
   '28/02/2020' : _29_02,
   '29/02/2020' : _29_02,
} 
   

