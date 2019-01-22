# coding=utf-8
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

def anna_rivi(n):
    rivi = []
    for x in range(n):
        while (True):
            uusi_luku = int(raw_input(str(rivi) + " - anna lottonumero: "))
            if (uusi_luku < min_arvo) or (uusi_luku > max_arvo):
                print ("Lottonumeron pitää olla välillä %d-%d" % (min_arvo,max_arvo))
            else:
                if not (arvottu_jo(rivi, uusi_luku)):
                    rivi.append(uusi_luku)
                    break
                else:
                    print ("Lottonumero annettu jo")
    return rivi

print (anna_rivi(lotto_numeroita))