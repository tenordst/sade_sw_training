

from os import system, name 
from Heatpump import Log

# to:do
#   useamman login purku samalla kertaa
#   summary
# www.gpsinformation.org/dale/nmea.htm
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
# Date	        Time	Version	    BT1	BT1 Mean BT2 BT3 BT10	BT11 Calc Supply GM	Alarm	RELAYS PCA BASE	BT12	BT14	BT17Tot.int.add. Prio	BT6	BT50
# 2016-02-25	10:07:08	1199	-12	-20	    344	294	35	  -6        361	    -786	0	 7	            348	    613	    43	0	        30	    443	    205
# 2016-02-25	10:08:08	1199	-12	-20	    348	298	35	  -5        361	    -802	0	 7	            352	    617	    38	0	        30	    443	    205

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
