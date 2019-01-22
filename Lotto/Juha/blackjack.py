
#uupuu:
#ässä 1 tai 11, nyt aina 1
#
############################################################################################
# Project 2 - Blackjack Game
#
# In this project you will be creating a Complete BlackJack Card Game in Python.
#
# Here are the requirements:
#
#     You need to create a simple text-based BlackJack game
#     The game needs to have one player versus an automated dealer.
#     The player can stand or hit.
#     The player must be able to pick their betting amount.
#     You need to keep track of the player's total money.
#     You need to alert the player of wins, losses, or busts, etc...
#
# And most importantly:
#
#     You must use OOP and classes in some portion of your game. You can not just use functions in your game. 
#     Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
############################################################################################

alkusaldo=1000
panos=100

class korttipakka:
    numerot={'A1':1,'2 ':2,'3 ':3,'4 ':4,'5 ':5,'6 ':6,'7 ':7,'8 ':8,'9 ':9,'10':10,'J ':10,'Q ':10,'K ':10}
    maat=['\u2660', '\u2663', '\u2666', '\u2665']  # unicode-symbolit maille

    def __init__(self, kortit):
        self.kortit=kortit
        kkortit=[]
        count=0
        for i in korttipakka.numerot: # Korteista yhtenäinen lista
            for j in korttipakka.maat:
                kkortit.append(i+':'+j)
                count+=1
        self.kortit=kkortit

class pelaaja:
    def __init__(self,nimi='Erkki',saldo=1000,kortit=[]):
        self.nimi=nimi
        self.saldo=saldo
        self.kortit=kortit

def ruutu_cls():
    import os
    clear=lambda:os.system('cls')
    clear()

def aloitetaan():
    ruutu_cls()
    print('Blackjack säännöt:\n')
    print('Tavoite saada 21. Kuvakortit on 10, muut numeronsa mukaisesti.')
    print('Ässä voi olla joko 1 tai 11. Kahden kortin 21 on blackjack, ja antaa lisäbonuksen\n')
    print('Pelaaja pelaa ensin kätensä loppuun, sitten jakajan vuoro. Jakaja pyrkii minimissään 17:a.')
    print('Alkusaldo = ', alkusaldo, 'ja panos ', panos)
    nimi = input('\n\n\nMikäs oli pelaajan nimi?  ')
    return nimi

def alkuprinttaukset(nimi):
    print('OK hyvä,', nimi,'aloitetaan\n')
    print('Lähtösaldo: ',peluri.saldo,'\n')

def pakansekotus(pakka):
    from random import shuffle
    shuffle(pakka.kortit)
    return pakka

def jaa_aloitus(p,c,pa):
    jaakortti(peluri,pakka)
    jaakortti(tietokone,pakka)
    jaakortti(peluri,pakka)
    jaakortti(tietokone,pakka)

def jaakortti(p,pa):
    p.kortit.append(pakka.kortit[0])
    pa.kortit=pa.kortit[1:]
    
def tulosta_kortit():
    print('Pelaajan käsi: \t\t ',*peluri.kortit, sep=' | ', end=' |')
    if tietokone.kortit==[]:
        print('\nCompuutterin käsi: \t  | \u2588 :\u2588',*a[1:], sep=' | ', end=' |')
    else:
        print('\nCompuutterin käsi: \t  | \u2588 :\u2588',*tietokone.kortit[1:], sep=' | ', end=' |')

def tulosta_kortit_loppu():
    print('Pelaajan käsi: \t\t ',*peluri.kortit, sep=' | ', end=' |')
    print('\nCompuutterin käsi:  \t ',*tietokone.kortit, sep=' | ', end=' |')
 
def tulos(p):
    summa=0
    counti=0
    for i in p.kortit:
        summa+=korttipakka.numerot[p.kortit[counti].split(':')[0]]
        counti+=1
    return summa

def lopputulos(p):
    summa=0
    counti=0
    for i in p.kortit:
        summa+=korttipakka.numerot[p.kortit[counti].split(':')[0]]
        counti+=1
    if any("A1" in s for s in p.kortit):
        if summa+10>21:
            pass
        else:
            summa+=10
    return summa


def tsekkaa_tulos(p):
    if tulos(p)>21:
        return 'yli'
    else:
        return tulos(p)

def seuraava_liike():
    while True:
        print('\nUusi kortti (U) vai pass (P)?')
        x=input().upper()
        if x=='U' or x=='P':
            break
    ruutu_cls()
    return x

def computer_vuoro():
    while lopputulos(tietokone) and lopputulos(tietokone)<17:
        jaakortti(tietokone,pakka)
    if tulos(tietokone)>21:
        return 'yli'

def tsekkaa_voittaja():
    ##testi blackjack##peluri.kortit=['A1:♣', 'K :♠']#####
    if lopputulos(tietokone)<22:
        if lopputulos(peluri)<lopputulos(tietokone) or lopputulos(peluri)>21:
            print(peluri.nimi+',',peluri.nimi+',','sie hävisit!\n')
            tulosta_kortit_loppu()
            print('\n')
           # peluri.saldo-=alkupanos
        elif (lopputulos(peluri) > lopputulos(tietokone)):
            print(peluri.nimi,'sie voitit!\n')
            tulosta_kortit_loppu()
            print('\n')
            if len(peluri.kortit)==2 and lopputulos(peluri)==21:
                print('Blackjack!')
                peluri.saldo+=panos*2
            peluri.saldo+=panos*2
        elif lopputulos(tietokone)==lopputulos(peluri):
            print('Tasapeli!\n')
            tulosta_kortit_loppu()
            print('\n')
        else:
            pass
    else:
        print(peluri.nimi,'sie voitit!\n')
        tulosta_kortit_loppu()
        print('\n')
        if len(peluri.kortit)==2 and lopputulos(peluri)==21:
            print('Blackjack!')
            peluri.saldo+=panos*2
        peluri.saldo+=panos*2

def jatketaanko():
    while True:
        print("\nJatketaanko, Y/N ?")
        j=input().upper()
        if j=='Y' or j=='N':
            break
    return j

#main
jatkuuko_main='True'
kortit=[]
while jatkuuko_main:
    nimi=aloitetaan() #kysytään nimi
    pakka=korttipakka(kortit) #jäljellä olevat kortit
    pakka=pakansekotus(pakka)  #sekoitetaan pakka
    pakka_temp=pakka.kortit[:] # varapakka
    pkasi,ckasi=[],[]  #pelaajien käet, tarvitaan initialisointiin?
    peluri=pelaaja(nimi,alkusaldo,pkasi)  # luodaan pelaaja annetulla nimellä, alkusaldo
    tietokone=pelaaja('Computer',alkusaldo,ckasi)
    ruutu_cls() # clear screen
    alkuprinttaukset(nimi)

    jatkuuko_peli='True'
    while jatkuuko_peli:
        peluri.saldo-=panos

        #x=input()
        if len(pakka.kortit)<10:
            pakka.kortit=pakka_temp[:] # uusi pakka käyttöön, kun vanha loppumassa
            pakka=pakansekotus(pakka)
        ruutu_cls()
        jaa_aloitus(peluri, tietokone, pakka) # aloituskortit, 2 molemmille
        tulosta_kortit()

        if tsekkaa_tulos(peluri)==('yli'):
            print('Tulos yli!\n')
            continue

        print('\n\nKorttisumma pelaaja: ',tulos(peluri))
        print('Saldo: ',peluri.saldo)

        #jatkuuko_peli='True'
        while seuraava_liike()== 'U':
            jaakortti(peluri,pakka)
            #print(peluri.kortit)
            if tsekkaa_tulos(peluri)=='yli':
                break
            tulosta_kortit()
            print('\n\nKorttisumma: ',peluri.nimi,tulos(peluri))
            print('Saldo: ',peluri.saldo)
        if tsekkaa_tulos(peluri)!='yli':
            computer_vuoro()

        tsekkaa_voittaja()
        if jatketaanko()=='Y' and peluri.saldo>=100:
            peluri.kortit=[]
            tietokone.kortit=[]
            ruutu_cls()
            continue
        elif peluri.saldo<100:
            print('Rahat loppu!\n')
            x=input('Paina enter..')
            exit()
        else:
            #jatkuuko_peli='False'
            print('Loppusaldo: ',peluri.saldo,'\n\n')
            x=input("Paina enter")
            exit()

