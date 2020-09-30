from Italia import *
from Spagna import *
day = input("Insert here the date you want see the info e.g. 24/03/2020\n")
nation = str(input("Insert here your nation\n"))
if nation == "Italy":
   try:
      Italia[day](day)
   except:
       print(default)
elif nation == "Spain":
   try:
      Spagna[day](day)
   except:
       print(default)       
else:
    print("Unknown input")