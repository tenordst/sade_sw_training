class Peli:
    nimi = ""

    def arvo(self):
        return "Sorry, en tiedä mitä arpoisin. "

class Lotto(Peli):
    nimi = "Lotto"

    def arvo(self):        
        return super(Lotto, self).arvo() + "Arvotaan Loton viikko 5 numerot"

class Keno(Peli):
    nimi = "Keno"

    def arvo(self):
        return "Kenossa ei tällä viikolla arvontaa"

lotto = Lotto()
keno = Keno()

print (lotto.arvo())
print (keno.arvo())