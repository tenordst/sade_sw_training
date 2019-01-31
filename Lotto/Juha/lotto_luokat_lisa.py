# import random
import os

#from lotto_luokat_lisa import lottorivi
from lotto_luokat_lisa import kayttaja
from lotto_luokat_lisa import tarkastaja

lottoajia=100000

def arvo_muut_kayttaja_tulokset(n):
    pelaajat=list()
    for i in range(n): #tehdään ziljoona pelaajaobjektia, ja niille arvotaan numerot
        pelaajat.append(kayttaja.kayttaja(str(i)))
        pelaajat[i].arvo_rivi()
    return pelaajat    

#main
# clear screen
clear = lambda: os.system('cls')
clear()

nimi=input("Terve! Anna nimesi niin aloitetaan: ")
erkki=kayttaja.kayttaja(nimi)
erkki.anna_rivi()
erkki.omarivi.tulosta(f'\n{erkki.nimi}, sun rivi oli: ')

kone=kayttaja.kayttaja("Kone")  
kone.arvo_rivi()        
kone.omarivi.tulosta('Ja oikea rivi oli: ')

tarkkis=tarkastaja.tarkastaja()
oikeita=tarkkis.kerro_tulos(erkki.omarivi.rivi,kone.omarivi.rivi)  

muut_pelaajat=arvo_muut_kayttaja_tulokset(lottoajia)
tarkkis.kerro_tulos_massat(muut_pelaajat, kone.omarivi.rivi,lottoajia,oikeita) 
