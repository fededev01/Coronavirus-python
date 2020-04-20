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
from Asia.Nepal import NPg25m01
from Asia.Singapore import SGg25m01
from Oceania.Australia import AUg25m01
from America.USA import USg25m01
from Europe.France import FRg25m01
from util.world import COMg25m01

print("Input a nation you want know about.\n")
print("You can also choose for info about the whole world.\n")
nation = input("Write the nation name in english:\n")
nationacc()
nowmonth()
month=input("Write the month in english with first letter maiusc\n")
nowday()
day=int(input("Write the number of the day\n"))

#China
#CN
#---------------------------------
#January
if nation=="China" and month=="January" and day==21:
 deaths()
 print(CNg21m01[0])
 confirmed()
 print(CNg21m01[1])
elif nation=="China" and month=="January" and day==22:
 deaths()
 print(CNg22m01[0])
 confirmed()
 print(CNg22m01[1])
elif nation=="China" and month=="January" and day==23:
 deaths()
 print(CNg23m01[0])
 confirmed()
 print(CNg23m01[1]) 
elif nation=="China" and month=="January" and day==24:
 deaths()
 print(CNg24m01[0])
 confirmed()
 print(CNg24m01[1])
elif nation=="China" and month=="January" and day==25:
 deaths()
 print(CNg25m01[0])
 confirmed()
 print(CNg25m01[1])
 #South Korea
 #KR
 #---------------------------------------
 #January
elif nation=="South Korea" and month=="January" and day==21:
 deaths()
 print(KRg21m01[0])
 confirmed()
 print(KRg21m01[1])
elif nation=="South Korea" and month=="January" and day==22:
 deaths()
 print(KRg22m01[0])
 confirmed()
 print(KRg22m01[1])
elif nation=="South Korea" and month=="January" and day==23:
 deaths()
 print(KRg23m01[0])
 confirmed()
 print(KRg23m01[1]) 
elif nation=="South Korea" and month=="January" and day==24:
 deaths()
 print(KRg24m01[0])
 confirmed()
 print(KRg24m01[1])
elif nation=="South Korea" and month=="January" and day==25:
 deaths()
 print(KRg25m01[0])
 confirmed()
 print(KRg25m01[1])
#Thailand
#TH
#------------------------------------------ 
#January
elif nation=="Thailand" and month=="January" and day==21:
 deaths()
 print(THg21m01[0])
 confirmed()
 print(THg21m01[1])
elif nation=="Thailand" and month=="January" and day==22:
 deaths()
 print(THg22m01[0])
 confirmed()
 print(THg22m01[1])
elif nation=="Thailand" and month=="January" and day==23:
 deaths()
 print(THg23m01[0])
 confirmed()
 print(THg23m01[1]) 
elif nation=="Thailand" and month=="January" and day==24:
 deaths()
 print(THg24m01[0])
 confirmed()
 print(THg24m01[1])
elif nation=="Thailand" and month=="January" and day==25:
 deaths()
 print(THg25m01[0])
 confirmed()
 print(THg25m01[1])
#Japan
#JP
#------------------------------------------ 
#January
elif nation=="Japan" and month=="January" and day==21:
 deaths()
 print(JPg21m01[0])
 confirmed()
 print(JPg21m01[1])
elif nation=="Japan" and month=="January" and day==22:
 deaths()
 print(JPg22m01[0])
 confirmed()
 print(JPg22m01[1])
elif nation=="Japan" and month=="January" and day==23:
 deaths()
 print(JPg23m01[0])
 confirmed()
 print(JPg23m01[1]) 
elif nation=="Japan" and month=="January" and day==24:
 deaths()
 print(JPg24m01[0])
 confirmed()
 print(JPg24m01[1])
elif nation=="Japan" and month=="January" and day==25:
 deaths()
 print(JPg25m01[0])
 confirmed()
 print(JPg25m01[1])
#Vietnam
#VN
#------------------------------------------ 
#January
elif nation=="Vietnam" and month=="January" and day==24:
 deaths()
 print(VNg24m01[0])
 confirmed()
 print(VNg24m01[1])
elif nation=="Vietnam" and month=="January" and day==25:
 deaths()
 print(VNg25m01[0])
 confirmed()
 print(VNg25m01[1])
#Singapore
#SG
#------------------------------------------ 
#January
elif nation=="Singapore" and month=="January" and day==24:
 deaths()
 print(SGg24m01[0])
 confirmed()
 print(SGg24m01[1])
elif nation=="Singapore" and month=="January" and day==25:
 deaths()
 print(SGg25m01[0])
 confirmed()
 print(SGg25m01[1])
#Nepal
#NP
#------------------------------------------ 
#January
elif nation=="Nepal" and month=="January" and day==25:
 deaths()
 print(NPg25m01[0])
 confirmed()
 print(NPg25m01[1])
#Australia
#AU
#------------------------------------------ 
#January
elif nation=="Australia" and month=="January" and day==25:
 deaths()
 print(AUg25m01[0])
 confirmed()
 print(AUg25m01[1])
#France
#FR
#------------------------------------------ 
#January
elif nation=="France" and month=="January" and day==25:
 deaths()
 print(FRg25m01[0])
 confirmed()
 print(FRg25m01[1])
#USA
#US
#------------------------------------------ 
#January
elif nation=="USA" and month=="January" and day==23:
 deaths()
 print(USg23m01[0])
 confirmed()
 print(USg23m01[1]) 
elif nation=="USA" and month=="January" and day==24:
 deaths()
 print(USg24m01[0])
 confirmed()
 print(USg24m01[1])
elif nation=="USA" and month=="January" and day==25:
 deaths()
 print(USg25m01[0])
 confirmed()
 print(USg25m01[1]) 
#World
#COM
#---------------------------------
#January
if nation=="World" and month=="January" and day==21:
 deaths()
 print(COMg21m01[0])
 confirmed()
 print(COMg21m01[1])
elif nation=="World" and month=="January" and day==22:
 deaths()
 print(COMg22m01[0])
 confirmed()
 print(COMg22m01[1])
elif nation=="World" and month=="January" and day==23:
 deaths()
 print(COMg23m01[0])
 confirmed()
 print(COMg23m01[1]) 
elif nation=="World" and month=="January" and day==24:
 deaths()
 print(COMg24m01[0])
 confirmed()
 print(COMg24m01[1])
elif nation=="World" and month=="January" and day==25:
 deaths()
 print(COMg25m01[0])
 confirmed()
 print(COMg25m01[1])                    
else:
 print("Unknown input")           