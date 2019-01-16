import random       
max_arvo =39
min_arvo=1
lotto_numeroita=7
lotto_lisanumeroita=3

def arvo_rivi(n):
    rivi =[]
    for x in range(n):
        rivi.append(random.randint(min_arvo, max_arvo))
    return rivi

print(arvo_rivi(lotto_numeroita))
