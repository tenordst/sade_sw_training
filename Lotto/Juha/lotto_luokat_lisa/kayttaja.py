from lotto_luokat_lisa import lottorivi


class kayttaja(): #pelaajajaobjekti, myös kone
    def __init__(self,nimi):
        self.nimi=nimi
        self.omarivi=lottorivi.lottorivi() #tallennetaan oma rivi
    def anna_rivi(self):
        self.omarivi.lisaa_numerot()
        return self.omarivi
    def arvo_rivi(self):
        self.omarivi.arvo_numerot()        
