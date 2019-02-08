

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
    # for windows 
    if name == 'nt': 
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

##################### Main ###############
clear()

# Määrittää lämpötilan jolloin pumpun tulkitaan olevan päällä
kaivo_meno_raja = 2 # 0.2C
lisalampo_raja = -400
pumppu_kaynnistyy = -60
pumppu_pysahtyy = 0

print('Hakee heatpump log-fileistä tiedot, ja tallentaa sekä plottaa kuvat ')
print('File-sijainnit: data-hakemistossa input logs (*.LOG), csv-hakemistoon tulostuu csv ja kuvat-hakemistoon png\n')

loki =Log.Log()
loki.lue_logi()
loki.plottaa()
loki.korjaa_csv_pilkut()
