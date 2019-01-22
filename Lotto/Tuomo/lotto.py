import random

min_arvo = 1
max_arvo = 39
lotto_numeroita = 7
lotto_lisänumerot = 3


def arvo_rivi(n):
    rivi = []
    for x in range(n):
        
        while True:
            uusi_numero = random.randint(min_arvo,max_arvo)
            if not uusi_numero in rivi:
                rivi.append(uusi_numero)
                break
            print ("uusiks meni")
        
    return rivi

print (arvo_rivi(lotto_numeroita))
