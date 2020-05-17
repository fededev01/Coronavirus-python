from util.functions import deaths
from util.functions import confirmed
from util.functions import nowmonth
from util.functions import nowday
from util.functions import monthacc
from util.functions import nationacc


#21 gennaio 2020
from Asia.China import CNg21m01
from Asia.South_Korea import KRg21m01
from Asia.Thailand import THg21m01
from Asia.Japan import JPg21m01
from util.world import COMg21m01

#22 gennaio 2020
from Asia.China import CNg22m01
from Asia.South_Korea import KRg22m01
from Asia.Thailand import THg22m01
from Asia.Japan import JPg22m01
from util.world import COMg22m01

#23 gennaio 2020
from Asia.China import CNg23m01
from Asia.South_Korea import KRg23m01
from Asia.Thailand import THg23m01
from Asia.Japan import JPg23m01
from America.USA import USg23m01
from util.world import COMg23m01

#24 gennaio 2020
from Asia.China import CNg24m01
from Asia.South_Korea import KRg24m01
from Asia.Thailand import THg24m01
from Asia.Japan import JPg24m01
from Asia.Vietnam import VNg24m01
from Asia.Singapore import SGg24m01
from America.USA import USg24m01
from util.world import COMg24m01

#25 gennaio 2020
from Asia.China import CNg25m01
from Asia.South_Korea import KRg25m01
from Asia.Thailand import THg25m01
from Asia.Japan import JPg25m01
from Asia.Vietnam import VNg25m01
from Asia.Singapore import SGg25m01
from Oceania.Australia import AUg25m01
from America.USA import USg25m01
from Europe.France import FRg25m01
from util.world import COMg25m01

print("Input a nation you want know about.\n")
print("You can also choose for info about the whole world")
nation = input("Write the nation name in english:\n")

if nation=="China":
    nationacc()
    nowmonth()
    month=input("Write the month in english with first letter maiusc")
    if month=="January":
        nowday()
        day=input("Write the number of the day")
        if day==21:
            deaths()
            print(CNg21m01[0])
            confirmed()
            print(CNg21m01[1])
        elif day==22:
            deaths()
            print(CNg22m01[0])
            confirmed()
            print(CNg22m01[1])
        elif day==23:
            deaths()
            print(CNg23m01[0])
            confirmed()
            print(CNg23m01[1])
        elif day==24:
            deaths()
            print(CNg24m01[0])
            confirmed()
            print(CNg24m01[1])
        elif day==25:
            deaths()
            print(CNg25m01[0])
            confirmed()
            print(CNg25m01[1])             
else:        
    if nation=="South Korea":
      nowmonth()
    if nation=="Thailand":
      nowmonth()
    if nation=="Japan":
      nowmonth()    
    if nation=="Vietnam":
      nowmonth()   
    if nation=="Singapore":
      nowmonth()    
    if nation=="Australia":
      nowmonth()    
    if nation=="USA":
      nowmonth()    
    if nation=="France":
      nowmonth()   
    if nation=="World":
      nowmonth()
    else:
      print("Unknown input")       
    
    
           