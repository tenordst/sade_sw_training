from lotto_luokat_lisa import lottorivi
from lotto_luokat_lisa import kayttaja


class tarkastaja():
    def __init__(self): #default potti ja voitonjakokertoimet
        self.voittopotti=10000000
        self.kertoimet=[0,0,0.02,0.03,0.05,0.1,0.8]
        self.voitonjako=[x*self.voittopotti for x in self.kertoimet]

    def kerro_tulos(self,annettu_rivi,oikea_rivi): #tsekataan oma tulos vs oikea rivi
        lkm=0
        for i in annettu_rivi:
            if i in oikea_rivi:
                lkm+=1
        print('\nOikeita numeroita sinulla oli',lkm,'\nLottoarvonnassa tällä viikolla oikeita tuloksia löytyi seuraavasti:\n')
        return lkm
    def kerro_tulos_massat(self,pelaaja_lista, oikea_rivi,n,oikeita): #ziljoonan pelaajan tulostsekkaus
        yhteiset=[]
        for i in range(n):
            yhteiset.append(len(list(set(pelaaja_lista[i].omarivi.rivi).intersection(oikea_rivi))))
        oikeiden_maara=[]
        for e in range(1,8):
            if yhteiset.count(e)>0:
                oikeiden_maara.append(yhteiset.count(e))
            else:
                oikeiden_maara.append(10000000000)
        voitot=[a/b for a,b in zip(self.voitonjako,oikeiden_maara)]
        voitot =[round(i) for i in voitot]
        for e in range(7,2,-1):
            print(f'{e} oikein tuloksia:\t', yhteiset.count(e))
        print('\n')      
        for e in range(7,2,-1):
            print(f'Voitto-osuudet: {e} oikein',voitot[e-1],'€')
        print(f'\nSinä voitit: ',voitot[oikeita-1],'€, onnittelut!!!!!\n')
        