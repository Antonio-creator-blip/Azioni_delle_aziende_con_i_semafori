import threading
import time
import random

print("---------------AZIONI IN BORSA-------------------- \n\n\n")

lista_aziende=[]

for i in range(10):
    #nome_azienda=input(f"Inserisci il nome dell'azienda numero {i+1} : ")
    nome_azienda=1
    lista_aziende.append(nome_azienda)
print("")




azione = 0

def calcolo(azienda):

    global azione
    
    azione=random.randint(1,10)
    

    
start = time.perf_counter()
def ricezione(random_azione,nome):
    print("La quotazione delle azioni in borsa dell'azienda {0} è {1}".format(nome,random_azione))

lista_thread=['Thread Uno','Thread Due', 'Thread Tre']
lista_first=[]
lista_second=[]
lista_third=[]
j=0
while(len(lista_first)<10 and len(lista_second)<10 and len(lista_third)<10):
    p=threading.Thread(target=calcolo, args=[i])
    p.start()
    p.join()
    i=0
    for i in range (10):
        j = random.randint(0,2)
        t=threading.Thread(target=ricezione, args=[azione,i])
        t.start()
        t.join()
        if(lista_thread[j] == 'Thread Uno'):
            lista_first.append(azione)
            print("Aggiunto a Thread Uno")
        
        elif(lista_thread[j] == 'Thread Due'):
            lista_second.append(azione)
            print("Aggiunto a Thread Due")
        
        else:
            lista_third.append(azione)
            print("Aggiunto a Thread Tre")


if(len(lista_first)>9):
    print("Ha vinto la lista numero Uno")
    print(lista_first)
        
elif(len(lista_second)>9):
    print("Ha vinto la lista numero Due")
    print(lista_second)
        
else:
    print("Ha vinto la lista numero Tre")
    print(lista_third)



    
#finish = time.perf_counter()

#print(finish-start)
