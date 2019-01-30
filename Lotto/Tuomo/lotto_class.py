# coding=utf-8
import random


class lottoRivi:
    #yleiset määrittelyt
    min = 1
    max =39
    pituus = 7


    def __init__(self):
        self.rivi = []

    def lisaa_numero(self, numero):
        if (numero < self.min or numero > self.max):
            print ("Numero %d ei ole lukuvälillä %d - %d" % (numero, self.min, self.max ))
            return False

        if (numero in self.rivi):
            print ("Numero %d on jo rivissä" % numero)
            return False

        self.rivi.append(numero)
        return True


    def tulosta_rivi(self, prefix):
        print(prefix + " " + str(self.rivi))
    

    def vertaile(self, toinen_rivi):
        oikein = 0
        for x in self.rivi:
            for y in toinen_rivi.rivi:
                if x == y:
                    oikein = oikein + 1
        return oikein



        

         




class LottoKone:

    def __init__(self):

        self.malli = "Mark II"

    def arvo_rivi(self):
        arvottu_rivi = lottoRivi()

        for x in range(arvottu_rivi.pituus):
            while True:
                arvottu_luku = random.randint(arvottu_rivi.min, arvottu_rivi.max)
                if (arvottu_rivi.lisaa_numero(arvottu_luku)):
                    break
        
        return arvottu_rivi
                    

    def anna_rivi(self):
        annettu_rivi = lottoRivi()

        for x in range(annettu_rivi.pituus):
            while True:
                annettu_luku = int(input(str(annettu_rivi.rivi) + "- anna lottonumerot välillä %s - %s : " % (annettu_rivi.min, annettu_rivi.max)))
                if (annettu_rivi.lisaa_numero(annettu_luku)):
                    break

        return annettu_rivi


class Kayttaja:

    def __init__(self, nimi):

        self.nimi = nimi
           


class Tarkistaja:

    def __init__(self, potti):
        self.potti = potti

    def kerro_tulos(self, kayttaja, rivi_a, rivi_b):
        oikein = rivi_a.vertaile(rivi_b)
        print ("Onneksi olkoon %s, sait %d oikein" % (kayttaja.nimi, oikein))








lotto = lottoRivi()
kone = LottoKone()
arvottu_rivi = kone.arvo_rivi()
kayttaja = Kayttaja("Tuomo")
annettu_rivi = kone.anna_rivi()
arvottu_rivi.tulosta_rivi("Arvottu rivi ")
annettu_rivi.tulosta_rivi("Annettu rivi ")
tarkistaja = Tarkistaja("1000000")
tarkistaja.kerro_tulos(kayttaja, annettu_rivi, arvottu_rivi)

