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

def vertaile_rivit(rivi1, rivi2):
    oikein = 0
    return oikein

annettu_rivi = anna_rivi(lotto_numeroita)
print ("Annettu rivi " + str(annettu_rivi))
arvottu_rivi = arvo_rivi(lotto_numeroita)
print ("Arvottu rivi " + str(arvottu_rivi))

oikein = vertaile_rivit(annettu_rivi, arvottu_jo)
print ("Onneksi olkoon, sait %d oikein" % oikein)