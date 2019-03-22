# coding=utf-8
import sys
import random
import csv
import locale
import datetime
import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


ulkolampotila = 'BT1'
vesi = 'BT2'
MaaMeno = 'BT11'
MaaTulo = 'BT10'
aika = 'Time'
paiva ='Date'





#print('Arguments:', len(sys.argv))
#print('List:', (sys.argv))

#tarkasta onko argumentti annettu ja jos on, niin luo polku
while True:
    if len(sys.argv) > 1:
        #print('annoit argumentin') 
        path = sys.argv[1] + '/'
        #print(path)
        break
    else:
        print('et antanut argumenttia')
        print('yritä uudestaan')
        path = 'data/'
        #exit()
        break

#lue tiedostonimet annetusta hakemistosta listaan
f = os.listdir(path)
kappale = len(f)
#print(kappale)
#print(f)
#print(f[1])

#lue tiedot tiedostosta
#df = pd.read_csv(path + f[0], sep='\t', skiprows=1)
#df1 = pd.read_csv(path + f[1], sep='\t', skiprows=1)
#dfa = pd.DataFrame(df)
#dfb = pd.DataFrame(df1)

#frames =[dfa, dfb]
#dfx = pd.concat(frames, ignore_index=True)
#print (df.head())
#print (dfx)



def sumfile(path):
    #lue kaikki tiedostot samaan taulukkoon
    f = os.listdir(path) #tiedostonimet annetusta hakemistosta
    kappale = len(f) # annettujen tiedostojen määrä
    df1= pd.read_csv(path + f[0], sep='\t', skiprows=1) # luetaan ensimmäinen tiedosto, josta tehdään tyhjä dataframe df1 jossa pelkkä otsikkorivi
    df1= pd.DataFrame(df1)
    df1= df1.head(0)
    #print(df1)
    df1 = pd.DataFrame(df1)
    #print (df1)
    for x in range(kappale): 
        #print(x)
        df2= pd.read_csv(path + f[x], sep='\t', skiprows=1)
        df = pd.DataFrame(df2)
        frames = [df1, df]
        #print (frames)
        dfx = pd.concat(frames, ignore_index=True)
        df1 = dfx
    return dfx   

def CsvByDate(file, path):
    # talleta päivät omiin CSV tiedostoihin
    dates = file.Date.unique() #yksilölliset päivämäärät tiedostosta date sarakkeesta
    kappale = len(dates) # kuinka monta eri päivämäärää tiedostossa on
    for x in range(kappale):
        d1 = file.loc[file['Date'] == dates[x]] # tekee uuden dataframen tietyn päivämäärän mukaan
        d1.to_csv(dates[x], sep='\t')



def PlotByDate(file):
    
    # Tulosta annetun päivän tiedot
    dates = file.Date.unique() #yksilölliset päivämäärät tiedostosta date sarakkeesta
    print(' ')
    print('Tulostaa annetun päivän graaffin ja tallettaa sen .png kuvaksi')
    print('Anna jokin listassa oleva päivämäärä samassa muodossa')
    print(' ')
    print(dates)
    print(' ')
    
    a = True
    while a:
        p = input('anna yksi tai useampi päivämäärä listasta välilyönnillä erotettuna: ').split(" ")
        
        #print(p)
        pituus = len(p)
        #print(pituus)
        for x in range(pituus):
            if p[x] in dates:
                #print('oikein')
                #print(x)
                a = False
                
            
            else:
                print('antamasi päivämäärä ei ole listassa, tai se oli väärässä muodossa')
                print('yritä uudestaan.....')
                a = True
                break
        
    #------------------------------------------------------------------------------------------  
                   

    #------------------------------------------------------------------------------------------        
    b = '' #tyhjä stringi png tiedoston nimeä varten
    kappale = len(p)
    if kappale == 1:
        d = file.loc[file['Date'] == p[0]] # tekee uuden dataframen tietyn päivämäärän mukaan
        b = p[0]
    else:
        a = []
        d1 = pd.DataFrame(a)
        for x in range(kappale):
            d = file.loc[file['Date'] == p[x]] # tekee uuden dataframen tietyn päivämäärän mukaan
            frames = [d1, d]
            #print (frames)
            d = pd.concat(frames, ignore_index=True)
            b = b + '_' + p[x] #lisätään kaikki annetut päivämäärät yhdeksi stringiksi
            d1 = d


    d.index = np.arange(1, len(d) + 1)
    print(d.head())

    x = (d[paiva] + ' ' + d[aika]) #yhdistetään päivä ja aika x-akselia varten
    
    #x = d[aika] #yhdistetään päivä ja aika x-akselia varten
    l = d[ulkolampotila] / 10 # ulkolämpötila y-akselia varten
    v = d[vesi] / 10 # kattilaveden lämpötila
    
    
    #plot
    #fig = plt.figure(num=None, figsize=(10, 5))
    #ax1 = fig.add_subplot(1, 1, 1, title='kuva', xlabel="Aika")
    #ax1.plot(x, l/10, 'blue', x, v/10, 'green')   
    #ax1.legend(['Ulkolämpötila (C)','kattilavedenlämpö (C)'])

    plt.plot(x, l, 'blue', x, v, 'red', x, (d[MaaMeno] / 10), 'green', x, (d[MaaTulo] / 10), 'yellow')
    plt.legend(['Ulkolämpötila (C)','kattilavedenlämpö (C)'])
    plt.ylabel('Lämpötila')
    plt.xlabel('Aika')
    plt.xticks(range(0, x.size, 60), fontsize=8)
    plt.grid(True, linestyle='-.')



    


    #display the plot
    
    plt.show()

    #fig.savefig(b + '_' + '.png'
    #fig.clf()
    #plt.close(fig)










x = sumfile(path) #kokoaa saman hakemiston kaikki tiedostot yhdeksi dataframeksi


#CsvByDate(x, path) #tallettaa dataframesta päiväkohtaiset tiedostot .csv formaattiin

PlotByDate(x) # piirtää dataframesta annetun päivämäärän käyrän ja png kuvan
