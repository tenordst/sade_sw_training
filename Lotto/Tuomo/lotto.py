# 
import random

min_arvo = 1
max_arvo = 39
lotto_numeroita = 7
lotto_lisänumerot = 3


def arvottu_jo(rivi, uusi):
    return uusi in rivi


def anna_rivi(n):
    rivi = []
    for x in range(n):
        
        while True:
            uusi_numero = int(input(str(rivi) + " - anna lottonumero valilla %s - %s " % (min_arvo, max_arvo)))
            if (uusi_numero < min_arvo) or (uusi_numero > max_arvo):
                print("Numero pitaa olla valilla %s - %s" % (min_arvo, max_arvo))
            else:
                if not (arvottu_jo(rivi, uusi_numero)) :            
                    rivi.append(uusi_numero)
                    break
                else:
                     print("luku on jo annettu")   
    return rivi
        
            
    

def arvo_rivi(n):
    rivi = []
    for x in range(n):
        
        while True:
            uusi_numero = random.randint(min_arvo,max_arvo)
            if not arvottu_jo(rivi, uusi_numero):
                rivi.append(uusi_numero)
                break
            print ("uusiks meni")
        
    return rivi



def vertaile_numerot (rivi1, rivi2):
    oikeat_numerot = []
    oikein = 0
    for x in rivi1:
        for y in rivi2:
            if x == y:
                oikeat_numerot.append(x)
                oikein = oikein + 1
    return oikein, oikeat_numerot







annettu = anna_rivi(lotto_numeroita)

for x in range(100):
    arvottu = arvo_rivi(lotto_numeroita)
    print ("++++")
    print (arvottu)
    print ("------")
    print (annettu)


    oikein, oikeat_numerot = vertaile_numerot(annettu, arvottu)
    print (oikein, " numeroa oli oikein")
    print ("seuraavat numerot olivat oikein ", oikeat_numerot)
    