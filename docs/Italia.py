from reader import *

def _22_01(x):
   print(dati['Italy'][0])
def _23_01(x):
   print(dati['Italy'][1])
def _24_01(x):
   print(dati['Italy'][2]) 
def _25_01(x):
   print(dati['Italy'][3])
def _26_01(x):
   print(dati['Italy'][4]) 
def _27_01(x):
   print(dati['Italy'][5]) 
def _28_01(x):
   print(dati['Italy'][6])
def _29_01(x):
   print(dati['Italy'][7])
def _30_01(x):
   print(dati['Italy'][8])
def _31_01(x):
   print(dati['Italy'][9])                
default = "Unknown input"    
    
Italia = {
   '22/01/2020' : _22_01,
   '23/01/2020' : _23_01,
   '24/01/2020' : _24_01,
   '25/01/2020' : _25_01,
   '26/01/2020' : _26_01,
   '27/01/2020' : _27_01,
   '28/01/2020' : _28_01,
   '29/01/2020' : _29_01,
   '30/01/2020' : _30_01,
   '31/01/2020' : _31_01,
}

if nation == "Italy":
   try:
      Italia[day](day)
   except:
       print(default)
else:
   pass          