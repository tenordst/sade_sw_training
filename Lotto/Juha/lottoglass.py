import random
import os

#jarjestelmaMax =11

class lottokone():
    def __init__(self):
        pass
    def arvottu_rivi(self,min_arvo,max_arvo,pituus):
        return random.sample(list(range(min_arvo,max_arvo)), pituus)

class lottorivi():
    min_arvo = 1
    max_arvo = 39
    pituus = 7

    def __init__(self):
        self.rivi=[]        
    def tulosta(self):
        print(self.rivi)
    def arvo_numerot(self):
        lottoarpoja=lottokone()
        self.rivi=lottoarpoja.arvottu_rivi(self.min_arvo,self.max_arvo,self.pituus)
    def lisaa_numerot(self):
        while True:
            print(f"\nAnna {self.pituus} numeroa väliltä {self.min_arvo}-{self.max_arvo}, erottele ne pilkulla (,) ja paina enter ")
            numerot = [int(x) for x in input().split(',')]
            if len(numerot)!=self.pituus or max(numerot)>self.max_arvo or min(numerot)<self.min_arvo:
                print('Väärää dataa, yritä uudelleen')
                numerot=[]
            else:
                break
        self.rivi=numerot
    def vertaile(self):
        pass

class kayttaja():
    def __init__(self,nimi):
        self.nimi=nimi
    def anna_rivi(self):
        annettu_rivi=lottorivi()
        annettu_rivi.lisaa_numerot()
        return annettu_rivi.rivi
    def arvo_rivi(self):
        pass

class tarkastaja():
    #def __init__(self, potti)
    def kerro_tulos(self,annettu_rivi,oikea_rivi):
        lkm=0
        for i in annettu_rivi:
            if i in oikea_rivi:
                lkm+=1
        return lkm

#main
# clear screen
clear = lambda: os.system('cls')
clear()

nimi=input("Terve! Anna nimesi niin aloitetaan: ")
erkki=kayttaja(nimi)
annettu_rivi=erkki.anna_rivi()

print(f'\n{erkki.nimi}, sun rivi oli: ', annettu_rivi)

oikea_rivi=lottorivi()
oikea_rivi.arvo_numerot()
print('Ja oikea rivi oli: ',oikea_rivi.rivi,'\n')

tarkkis=tarkastaja()
oikeita=tarkkis.kerro_tulos(annettu_rivi,oikea_rivi.rivi)
print("Oikeita numeroita löytyi: ",oikeita,'\n')




