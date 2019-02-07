# coding=utf-8
import sys
import random
import csv
import locale
import datetime
import os
import glob

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from os import system, name 

class Log():
    def __init__(self):
        self.loki=''  #input log nimi, xxx.LOG
        self.loppulista=[]
        # self.output_file='csv_output.csv'
        self.output_file=''        
        
    def lue_logi(self):
        self.tsekkaa_hakemistot("data/","csv/","kuvat/") #onko jo olemassa, jos ei niin luodaan
        fileet =glob.glob("data/*.LOG") #hakee hakemistossa olevat fileet
        for i,n in enumerate(fileet):
            print('Hakemistosta löytyy: ',fileet[i].split('\\')[1])
        self.loki=input('Anna LOG-tekstifile-nimi (data-hakemistossa): ')
        self.output_file=self.loki.split('.')[0] +'.csv'
        # output_file='csv_output.csv'
        myFile=open('./data/'+self.loki,mode='r') # luetaan nmea-file
        rivit=list(myFile.readlines())
        self.loppulista=self.pura_log(rivit)
        self.kirjoita_tiedostoon()

    def tsekkaa_hakemistot(self,a,b,c):
        if not os.path.exists(a):
            os.makedirs(a)
        if not os.path.exists(b):
            os.makedirs(b)
        if not os.path.exists(c):
            os.makedirs(c)

    def pura_log(self,line):
        output=[]
        count=0
        loppulista=[]
        for i in range(1,len(line)):    
            fields=line[i].split('\t')
            fields[-1]=fields[-1].strip()
            loppulista.append(fields)
        return loppulista

    def kirjoita_tiedostoon(self):
        otsikko =self.loppulista[0]
        otsikko[3]="Ulkolampotila_index"
        otsikko[5]="Lammitys_meno_index"
        otsikko[6]="Lammitys_tulo_index"
        otsikko[7]="Kaivo_tulo_index"
        otsikko[8]="Kaivo_meno_index"
        otsikko[9]="Laskettu_meno_index"
        otsikko[10]="Asteminuutit_index"
        otsikko[17]="Toimintatila_index"
        otsikko[18]="Kayttovesi_index"
        with open('./csv/'+self.output_file, "w") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(self.loppulista)
        f.close()

    def plottaa(self):
        df = pd.read_csv('./csv/'+self.output_file)
        tulo = df['Lammitys_tulo_index'] 
        meno = df['Lammitys_meno_index'] 
        kaivo_meno = df['Kaivo_meno_index'] 
        kaivo_tulo =df['Kaivo_tulo_index']
        ulko_lampo =df['Ulkolampotila_index']
        kayttovesilampo =df['Kayttovesi_index']
        tavoitearvot =df['Laskettu_meno_index']
        asteminuutit =df['Asteminuutit_index']

        # kaivo_meno=kaivo_meno.iloc[kaivo_meno.to_numpy().nonzero()] #nollat pois ennen laskelmaa
        kuvatus=plt.figure(figsize=(20, 10), dpi=100)    
        ax1 = kuvatus.add_subplot(1,1,1)
        ax2 = ax1.twinx()
        
        ax1_plotit=[tulo,meno,kaivo_tulo,kaivo_meno,ulko_lampo,kayttovesilampo,tavoitearvot]
        for i in range(7):
            ax1.plot(ax1_plotit[i],label=["Lämmitys tulo","Lämmitys meno","Kaivo tulo","Kaivo meno","Ulkolampo","Käyttövesi","Tavoitearvot"][i], lw=1)
        ax2.plot(asteminuutit, label="Asteminuutit", lw=1)
        ax1.legend(fontsize=10, loc="best")
        ax2.legend(fontsize=10, loc="best")
        plt.ylabel("Asteita", fontsize=10)
        ax1.set_ylabel("Asteita", fontsize=10) 
        ax1.set_xlabel("Aika", fontsize=10)   
        ax1.grid(True, which='major',color ="black",linestyle=':', linewidth=0.3)
        plt.title(self.loki,fontsize=12, color="darkred", loc="center")

        image_nimi=self.loki.split('.')[0]  #.csv-liite pois
        plt.savefig('./kuvat/'+image_nimi, bbox_inches='tight')
        plt.show()

    def korjaa_csv_pilkut(self):  
        with open('./csv/'+self.output_file, newline=None) as f:
            uusiTeksti=f.read()
        while ',' in uusiTeksti:
            uusiTeksti=uusiTeksti.replace(',',';')        
        with open('./csv/'+self.output_file, "w") as f:
            f.write(uusiTeksti)
        f.close()