import random

min_arvo = 1
max_arvo = 39
lotto_lisanumeroita = 3
lottoarvontoja = int(input("Tervetuloa lottoamaan, kuinka moneen arvontaan haluat osallistua?"))
lotto_numeroita = int(input("Millaisen järjestelmän haluat (7,8,9...numeroa): "))
def annettu_jo(oma_rivi, uusi_numero):
    return uusi_numero in oma_rivi

def syota_rivi(n):
    oma_rivi = []
    for x in range(n):   
        while(True):
            oma_luku = int(input("Anna numero:"))
            if not (annettu_jo(oma_rivi, oma_luku)):
                if min_arvo <= oma_luku <= max_arvo:
                    print ("Hyväksytty, anna seuraava")
                    oma_rivi.append(oma_luku)                        
                    break
                else:
                    print("luku ei ole välillä 1-39")
            else:
                print("Annettu jo")
    return oma_rivi

print("Anna %d numeroa väliltä 1-39 lottoarvontaa varten: " %lotto_numeroita)
                

def arvottu_jo(rivi, uusi):
    return uusi in rivi
        

def arvottu_rivi(n):
    rivi = []
    for x in range(n):
        while(True):
            uusi_luku = random.randint(min_arvo, max_arvo)
            if not (arvottu_jo(rivi, uusi_luku)):
                rivi.append(uusi_luku)
                break
    return rivi



def vertaile_rivit(rivi1, rivi2):
    oikein = 0
    for x in rivi1:
        for y in rivi2:
            if (x == y):
                oikein = oikein + 1
    return oikein   

oma_rivi = syota_rivi(lotto_numeroita)


arvonnat = 0
tilasto = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range (lottoarvontoja):
    arvonta = arvottu_rivi(7)
    lottonumerot = arvottu_rivi(lotto_numeroita)
    oikein = vertaile_rivit(oma_rivi, arvonta)
    tilasto[oikein] +=1
    print ("Arvotut numerot", arvonta)
    print ("oma rivisi:", oma_rivi)
    print ("Tilastot: 0 oikein, 1 oikein jne...", tilasto, " arvontoja %d" %arvonnat)
    if oikein == 7:
        print("Sää voitit!! Eikä mennyt kuin %d arvontaa" %arvonnat)
        break
    else:
        arvonnat = arvonnat + 1
        print ("Voe paska, sait vaan %d oikein" % oikein)

