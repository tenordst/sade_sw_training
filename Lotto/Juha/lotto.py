import random

min_arvo = 1
max_arvo = 39
lotto_numeroita = 7
lotto_lisanumeroita = 3
jarjestelma_koko =8

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

def jarjestelma_func(n):
    import os
    numerot=[]

    numerot = [int(x) for x in input("Anna %i numeroa väliltä 1-39, erottele ne pilkulla (,) ja paina enter "%n).split(',')]
    alilistat=sublists(numerot)
    county=0
    for i in alilistat:
        alilistat[county].sort()
        county+=1
    alilistat= sort_and_deduplicate(alilistat)
    return alilistat


def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item
    return lst

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))

def sublists(numerot):
    from itertools import permutations
    alilista=[]
    ind=0
    for i in permutations(numerot, 7):
        #print (i)
        alilista.append(list(i))
        ind+=1
    return alilista

import os
clear = lambda: os.system('cls')
clear()
jarjestelma=input('Anna järjestelmän koko: 7,8 tai 9 numeroa: ')

if jarjestelma=='7' or jarjestelma=='8' or jarjestelma=='9':
    kayttajan_numerot=[]
    kayttajan_numerot= jarjestelma_func(int(jarjestelma))
    oikea_rivi=arvo_rivi(lotto_numeroita)
    #print(kayttajan_numerot)
    county=0
    print('\nOikea rivi',oikea_rivi,'\n')
    for i in kayttajan_numerot:
        #print(kayttajan_numerot[county])
        print('Rivi:',i,'Oikeita:',laskeoikeat(i,oikea_rivi))
        county+=1
    print('\n')
else:
    print('Not valid')
