import os
import glob
from os import system, name 
from Heatpump import Log
from Heatpump import Summaa

def clear(): 
    if name == 'nt':     # for windows 
        _ = system('cls')     
    else:  # for mac and linux(here, os.name is 'posix') 
        _ = system('clear')

def tsekkaa_hakemistot(a,b,c):
    for i in [a,b,c]:
        if not os.path.exists(i):
            os.makedirs(i)

clear()
print('Hakee heatpump log-fileistä tiedot, ja tallentaa sekä plottaa kuvat ')
print('File-sijainnit: data-hakemistossa input logs (*.LOG), csv-hakemistoon tulostuu csv ja kuvat-hakemistoon png\n')

tsekkaa_hakemistot("data/","csv/","kuvat/")
fileet =glob.glob("data/*.LOG") #hakee hakemistossa olevat fileet, ei varmaan toimi macissä?
for i,n in enumerate(fileet):
    print('Hakemistosta löytyy: ',fileet[i].split('\\')[1]) # ei toimi macissä?
lokiNimi=input('\nAnna tiedoston nimi (esim 160225-1.LOG), tai kuukausi (1602): ')

loki =Log.Log(lokiNimi)
loki.lue_logi(fileet)
loki.plottaa(lokiNimi)

summa=Summaa.Summaa(lokiNimi)
summa.laskeJaPrinttaa()
summa.tulostaSummary()