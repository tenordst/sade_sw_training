import os
import glob
from os import system, name 
from Heatpump import Log

# to:do
#   useamman login purku samalla kertaa
#   summary
##############################################################################################################################
#  - Nibe lämpöpumpun logien analysointi
#       - Vaatimukset
#          - Kustakin päivittäisestä logitiedosta muodostetaan .png kuvaaja jossa näkyy eri parametrit visualisoituna kuvaajana
#          - Muodostetaan myös kuukausikohtainen summary kuvaaja josta näkyy per päivä halutut arvot
#             - Käynnistyskerrat
#       - Luokkarakenne
#       - Log .csv tiedoston lataaminen olioon, tarvittavia moduuleja/luokkia
#          - csv
#          - numpy
#          - panda
# - matplotlib
###########################################################################################################################

class Summary():
    def __init__(self):
        pass

def clear(): 
    if name == 'nt':     # for windows 
        _ = system('cls')     
    else:  # for mac and linux(here, os.name is 'posix') 
        _ = system('clear')

def tsekkaa_hakemistot(a,b,c):
    if not os.path.exists(a):
        os.makedirs(a)
    if not os.path.exists(b):
        os.makedirs(b)
    if not os.path.exists(c):
        os.makedirs(c)
##################### Main ###############
clear()
# Määrittää lämpötilan jolloin pumpun tulkitaan olevan päällä
kaivo_meno_raja = 2 # 0.2C
lisalampo_raja = -400
pumppu_kaynnistyy = -60
pumppu_pysahtyy = 0

print('Hakee heatpump log-fileistä tiedot, ja tallentaa sekä plottaa kuvat ')
print('File-sijainnit: data-hakemistossa input logs (*.LOG), csv-hakemistoon tulostuu csv ja kuvat-hakemistoon png\n')

tsekkaa_hakemistot("data/","csv/","kuvat/")
fileet =glob.glob("data/*.LOG") #hakee hakemistossa olevat fileet
for i,n in enumerate(fileet):
    print('Hakemistosta löytyy: ',fileet[i].split('\\')[1]) # ei toimi macissä?
lokiNimi=input('\nAnna tiedoston nimi (esim 160225-1.LOG), tai kuukausi (1602): ')

loki =Log.Log(lokiNimi)
loki.lue_logi(fileet)
loki.plottaa(lokiNimi)
loki.korjaa_csv_pilkut()
