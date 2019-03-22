# coding=utf-8
import sys
import random
import csv
import locale
import datetime

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Log csv tiedostojen indeksit
ulkolampotila_index = 3
ulkolampotila = 'BT1'
lammitys_meno_index = 5
lammitys_tulo_index = 6
kaivo_tulo_index = 7
kaivo_meno_index = 8
laskettu_meno_index = 9
asteminuutit_index = 10
toimintatila_index = 17
kayttovesi_index = 18

# Määrittää lämpötilan jolloin pumpun tulkitaan olevan päällä
kaivo_meno_raja = 2 # 0.2C
lisalampo_raja = -400
pumppu_kaynnistyy = -60
pumppu_pysahtyy = 0


#class log:
    #def __init__(self, file)


def draw_graphs(self, file):
    # plot the data
    fig = plt.figure(num=None, figsize=(16, 10), dpi=120)
    ax1 = fig.add_subplot(1, 1, 1, title=file, xlabel="Aika")
    #ax1.plot(self.t, self.kaivo_menolammot, 'blue',self.t, self.kaivo_tulolammot, 'green',  self.t, self.tulolammot, 'yellow',  self.t, self.menolammot, 'cyan', self.t, self.ulkolammot, 'grey', self.t, self.kayttovesilammot, 'magenta', self.t, self.tavoitearvot, 'black')
    ax1.plot(self.t, self.ulkolampotila, 'blue')
    #ax1.legend(['Kaivo meno (C)','Kaivo tulo (C)','Lämmitys tulo (C)', 'Lämmitys meno (C)', 'Ulkolämpö (C)', 'Käyttövesi (C)', 'Tavoitelämpö (C)'])
    ax1.legend(['Ulkolämpötila (C)'])
    #ax2 = ax1.twinx()
    #ax2.plot(self.t,self.asteminuutit, 'r')		
    #ax2.legend(['Asteminuutit'])
    fig.savefig(file + ".png")
    fig.clf()
    plt.close(fig)

path = '/'
print (sys.argv)
if len(sys.argv) > 1:
	path = path + sys.argv[1] + '/'

print(path)
print(sys.argv[1])

# Get list of of all files in the current dir
#from os import walk
#f = []
#for (dirpath, dirnames, filenames) in walk(path):
#	for filename in filenames:
#		f.append(path + filename)
#	break

#df = pd.read_csv(f[0], sep='\t', skiprows=1)
#print (df.head())
#print (df[ulkolampotila])


# matplotlibilla graafi joka näyttää ulkolämpötila

#print (df)


