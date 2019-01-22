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

print (arvo_rivi(lotto_numeroita))