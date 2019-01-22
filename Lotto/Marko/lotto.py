# coding=utf-8
import random
min_arvo = 1
max_arvo = 39
lotto_numeroita = 7
lotto_lisanumeroita = 3

def arvottu_jo(rivi, uusi):
    return uusi in rivi

def kysy_numerot(n):
    pelaajan_omat = []
    for i in range (n):
        while (True):
            pelaajan_luku = int(raw_input(str(pelaajan_omat) + "Anna lottonumeroita"))
            if not (arvottu_jo(pelaajan_omat, pelaajan_luku)):
                pelaajan_omat.append(pelaajan_luku)
                break
    return pelaajan_omat

# Kysytään annetut luvut
annetut_luvut = kysy_numerot(lotto_numeroita)
print (annetut_luvut)
        
def arvo_rivi(n):
    rivi = []
    for x in range(n):
        while (True):
            uusi_luku = random.randint(min_arvo, max_arvo)
            if not (arvottu_jo(rivi, uusi_luku)):
                rivi.append(uusi_luku)
                print ("hello")
                break
            print("world")
    return rivi
    

print (arvo_rivi(lotto_numeroita))
