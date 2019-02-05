import random


class lottokone():
    def __init__(self):
        pass
    def arvottu_rivi(self,min_arvo,max_arvo,pituus):
        return random.sample(list(range(min_arvo,max_arvo)), pituus)# palauttaa listan arvottuja numeroita