import random
min_arvo = 1
max_arvo = 39
lotto_numeroita = 7
lotto_lisanumeroita = 3

def arvottu_jo(rivi, uusi):
    return uusi in rivi

def kysy_numerot(pelaajan_omat, pelaajan_luku):
    pelaajan_omat = []
    for i in range (n):
        while (True):
            pelaajan_luku = int(raw_input(str(pelaajan_omat) + "Anna lottonumeroita"))
            if not (arvottu_jo(pelaajan_omat, pelaajan_luku)):
                pelaajan_rivi.append(pelaajan_luku)
                break
    return pelaajan_rivi

print (kysy_numerot(pelaajan_omat))
        

       

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
