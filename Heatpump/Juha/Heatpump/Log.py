# coding=utf-8
import sys
import csv
import locale
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
        self.output_file=''        
        
    def lue_logi(self):
        self.tsekkaa_hakemistot("data/","csv/","kuvat/") #onko jo olemassa, jos ei niin luodaan
        fileet =glob.glob("data/*.LOG") #hakee hakemistossa olevat fileet
        for i,n in enumerate(fileet):
            print('Hakemistosta löytyy: ',fileet[i].split('\\')[1])
        self.loki=input('Anna LOG-tekstifile-nimi (data-hakemistossa): ')
        self.output_file=self.loki.split('.')[0] +'.csv'
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
        tulo = df['Lammitys_tulo_index'] /10
        meno = df['Lammitys_meno_index'] /10
        kaivo_meno = df['Kaivo_meno_index'] /10
        kaivo_tulo =df['Kaivo_tulo_index'] /10
        ulko_lampo =df['Ulkolampotila_index'] /10
        kayttovesilampo =df['Kayttovesi_index'] /10
        tavoitearvot =df['Laskettu_meno_index'] /10
        asteminuutit =df['Asteminuutit_index'] /10

        # kaivo_meno=kaivo_meno.iloc[kaivo_meno.to_numpy().nonzero()] #nollat pois ennen laskelmaa
  
        fig,ax=plt.subplots(nrows=2,ncols=1,figsize=(20, 10), dpi=100)#figsize=(20, 10), dpi=100)            
        ax1_plotit=[tulo,meno,kayttovesilampo,tavoitearvot]
        for i in range(4):
            ax[0].plot(ax1_plotit[i],label=["Lämmitys tulo","Lämmitys meno","Käyttövesi","Tavoitearvot"][i], lw=1)
        ax[0].legend(fontsize=10, loc="best")
        plt.ylabel("Asteita", fontsize=10)
        ax[0].set_ylabel("Asteita", fontsize=10) 
        ax[0].set_xlabel("Aika", fontsize=10)   
        ax[0].grid(True, which='major',color ="black",linestyle=':', linewidth=0.3)
        ax[1].grid(True, which='major',color ="black",linestyle=':', linewidth=0.3)
        ax[1].plot(kaivo_tulo,label="Kaivo meno", lw=1)
        ax[1].plot(kaivo_meno,label="Kaivo tulo", lw=1)
        ax[1].plot(ulko_lampo,label="Ulkolämpö", lw=1)
        ax2=ax[1].twinx()
        ax2.plot(asteminuutit, label="Asteminuutit", c="black",lw=1)
        ax[1].legend(fontsize=10, loc="upper left")
        ax[0].legend(fontsize=10, loc="best")
        ax2.legend(fontsize=10, loc="best")
        plt.title(self.loki,fontsize=12, color="darkred", loc="center")
        image_nimi=self.loki.split('.')[0]  #.csv-liite pois
        plt.savefig('./kuvat/'+image_nimi, bbox_inches='tight')
        plt.tight_layout() 
        plt.show()

    def korjaa_csv_pilkut(self):  
        with open('./csv/'+self.output_file, newline=None) as f:
            uusiTeksti=f.read()
        while ',' in uusiTeksti:
            uusiTeksti=uusiTeksti.replace(',',';')        
        with open('./csv/'+self.output_file, "w") as f:
            f.write(uusiTeksti)
        f.close()