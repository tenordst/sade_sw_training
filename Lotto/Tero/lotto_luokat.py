# coding=utf-8
import random

class LottoRivi:
    # Yleiset määrittelyt
    min = 1
    max = 39
    pituus = 7

    def __init__(self):
        self.rivi = []

    def lisaa_numero(self, numero):
        if (numero < self.min or numero > self.max):
            # print ('Numero %d ei lukuvälillä' % numero)
            return False

        if (numero in self.rivi):
            # print ('Numero %d on jo rivissä' % numero)
            return False

        self.rivi.append(numero)
        return True

    def tulosta_rivi(self, prefix):
        print (prefix + ' ' + str(self.rivi))

    def vertaile(self, toinen_rivi):
        oikein = 0
        for x in self.rivi:
            for y in toinen_rivi.rivi:
                if (x == y):
                    oikein = oikein + 1
        return oikein

class LottoKone:

    def __init__(self):
        self.malli = 'Mark V'
        print ('Lottokone %s valmiina uusiin seikkailuihin' % self.malli)

    def arvo_rivi(self):
        arvottu_rivi = LottoRivi()

        for x in range(arvottu_rivi.pituus):
            while (True):
                arvottu_luku = random.randint(arvottu_rivi.min, arvottu_rivi.max)
                if (arvottu_rivi.lisaa_numero(arvottu_luku)):
                    break

        return arvottu_rivi

class Kayttaja:
    
    def __init__(self, nimi):
        self.nimi = nimi

    def anna_rivi(self):
        lottokone = LottoKone()
        annettu_rivi = lottokone.arvo_rivi()
        return annettu_rivi

class Tarkistaja:
    
    def __init__(self, potti):
        self.potti = potti

    def kerro_tulos(self, kayttaja, rivi_a, rivi_b):
        oikein = rivi_a.vertaile(rivi_b)
        print ('Onneksi olkoon %s, sait %d oikein' % (kayttaja.nimi, oikein))


kone = LottoKone()
arvottu_rivi = kone.arvo_rivi()
kayttaja = Kayttaja('Tero')
annettu_rivi = kayttaja.anna_rivi()
arvottu_rivi.tulosta_rivi('Arvottu rivi')
annettu_rivi.tulosta_rivi('Annettu rivi')
tarkistaja = Tarkistaja('10000000')
tarkistaja.kerro_tulos(kayttaja, annettu_rivi, arvottu_rivi)