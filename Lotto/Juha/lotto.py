import random

min_arvo = 1
max_arvo = 39
lotto_numeroita = 7
lotto_lisanumeroita = 3

def arvottu_jo(rivi, uusi):
    return uusi in rivi 

def arvo_rivi(n):
    rivi = []
    for x in range(n):
        while (True):
            uusi_luku = random.randint(min_arvo,max_arvo)
            if not (arvottu_jo(rivi, uusi_luku)):
                rivi.append(uusi_luku)
                break
    return rivi

def kysy_numerot(n):
    import os
    clear = lambda: os.system('cls')
    clear()
    numerot=[]
    numerot = [int(x) for x in input("Anna %i numeroa väliltä 1-39, erottele ne pilkulla (,) ja paina enter "%n).split(',')]

    return numerot

def laskeoikeat(kayttajan_numerot,oikea_rivi):
    lkm=0
    for i in kayttajan_numerot:
        if i in oikea_rivi:
            #print (i)
            lkm+=1
    return lkm

kayttajan_numerot= kysy_numerot(lotto_numeroita)
oikea_rivi=arvo_rivi(lotto_numeroita)
oikeiden_maara=laskeoikeat(kayttajan_numerot,oikea_rivi)
print ('Käyttäjän rivi',kayttajan_numerot)
print('Oikea rivi',oikea_rivi)
print('Oikeiden määrä',oikeiden_maara)

