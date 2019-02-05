# coding=utf-8
import sys
import random
import csv
import locale
import datetime

# import numpy as np
# import matplotlib.pyplot as plt

# Log csv tiedostojen indeksit
ulkolampotila_index = 3
lammitys_meno_index = 5
lammitys_tulo_index = 6
kaivo_tulo_index = 7
kaivo_meno_index = 8
laskettu_meno_index = 9
asteminuutit_index = 10
toimintatila_index = 17
kayttovesi_index = 18

# Määrittää lämpötilan jolloin pumpun tulkitaan olevan päällä
kaivo_meno_raja = 2
lisalampo_raja = -400
mittauksia = 1500

path = './'
if len(sys.argv) > 1:
	path = path + sys.argv[1] + '/'

# Get list of of all files in the current dir
from os import walk
f = []
for (dirpath, dirnames, filenames) in walk(path):
	for filename in filenames:
		f.append(path + filename)
	break

print (f)