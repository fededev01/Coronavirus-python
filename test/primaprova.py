genericlist = [positivi, morti, guariti, totali]
#in cui "positivi" sono "attualmente positivi" e "totali" sono "casi totali"
#genericlist è la lista generica


g21m01 = [1000, 500, 2500, 160000]
#in cui g21 è il numero 21 del mese indicato dopo m, 01 è gennaio, quindi 21 gennaio
#in cui il primo numero di g21m01 corrisponde alla prima stringa di genericlist
#in cui I numeri su rappresentanti corrispondono ai totali rilasciati dall'oms. La cui chiave di lettura è questa:
#Ad oggi ci sono 1000 persone che sono attualmente positive
#Ad oggi sono morte 500 persone

g22m01 = [2000, 100, 3000, 170000]
#in cui g22 è il numero 22 del mese indicato dopo m, 01 è gennaio, quindi 22 gennaio
#in cui il primo numero di g22m01 corrisponde alla prima stringa di genericlist
#in cui I numeri su rappresentanti corrispondono ai totali rilasciati dall'oms. La cui chiave di lettura è questa:
#Ad oggi ci sono 2000 persone che sono attualmente positive
#Ad oggi sono morte 1000 persone

print("Scrivi il nome del mese a cui vuoi accedere") 
print("Ci raccomandiamo di scrivere tutto minuscolo") 

print("Options:\n") 
print("Scrivi 'gennaio' se vuoi accedere ai bollettini del mese di gennaio") 
print("Scrivi 'febbraio' se vuoi accedere ai bollettini del mese di febbraio") 
print("Scrivi 'marzo' se vuoi accedere ai bollettini del mese di marzo") 
print("Scrivi 'aprile' se vuoi accedere ai bollettini del mese di aprile") 

primoinput  = input(" : \n")
print("Scrivi il numero del giorno a cui vuoi accedere")
print("Ci raccomandiamo di scrivere il numero a cifre") 


secondoinput  = input(" : \n")