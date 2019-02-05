from lotto_luokat_lisa import lottokone


class lottorivi():
    min_arvo = 1
    max_arvo = 39
    pituus = 7

    def __init__(self):
        self.rivi=[]        
    def tulosta(self,s):
        print(s,self.rivi)
    def arvo_numerot(self):
        lottoarpoja=lottokone.lottokone()
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