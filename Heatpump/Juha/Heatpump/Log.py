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
    def __init__(self,lokiNimi):
        self.lokiNimi=lokiNimi  #input log nimi, xxx.LOG
        self.lokiKuukausi=lokiNimi[:4]
        self.loppulista=[]
        self.output_file=''        
        
    def lue_logi(self, fileet):
        if len(self.lokiNimi) ==4:
            self.hoida_kuukausi(fileet)
            self.output_file=self.lokiNimi+'.csv' #.split('.')[0] +'.csv'
            myFile=open('./data/'+self.lokiNimi+'.LOG',mode='r') # luetaan file
            rivit=list(myFile.readlines())
            self.loppulista=self.pura_log(rivit)
            self.kirjoita_tiedostoon()
        else:
            self.hoida_kuukausi(fileet)
            self.output_file=self.lokiNimi[:-4]+'.csv' #.split('.')[0] +'.csv'
            myFile=open('./data/'+self.lokiKuukausi+'.log',mode='r') # luetaan file
            rivit=list(myFile.readlines())
            self.loppulista=self.pura_log(rivit)
            self.kirjoita_tiedostoon()
    def hoida_kuukausi(self,fileet):
        with open('./data/'+self.lokiKuukausi+'.log',"w") as outfile:
            outfile.write('')
        for i,n in enumerate(fileet):
            if ((n.split('\\')[1])[:4]) == self.lokiNimi[:4]:
                with open('./data/'+self.lokiKuukausi+'.log',"a") as outfile:
                    with open(n) as f1:
                        for line in f1:
                            outfile.write(line)
        f = open('./data/'+self.lokiKuukausi+'.log',"r")
        lines = f.readlines()
        f.close()
        f = open('./data/'+self.lokiKuukausi+'.log',"w")
        f.write(lines[0])
        f.write(lines[1])
        for line in lines:
            if not line.startswith("D"):
                f.write(line)

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

    def kirjoita_tiedostoon(self, tiedosto='',rivit=''):
        if tiedosto=='':
            tiedosto =self.output_file
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
        if len(self.lokiNimi)>4:
            temp=[otsikko]
            for i in self.loppulista[1:]:
                if i[0]==('20'+self.lokiNimi[:2]+'-'+self.lokiNimi[2:4]+'-'+self.lokiNimi[4:6]):
                    temp.append(i)
            self.loppulista=temp   
        
        with open('./csv/'+tiedosto, "w") as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerows(self.loppulista)
        f.close()

    def plottaa(self,lokiNimi):
        df1 = pd.read_csv('./csv/'+self.output_file)
        if len(self.lokiNimi) !=4: #annettu kuukausi
            filtteri='20'+lokiNimi[:2]+'-'+lokiNimi[2:4]+'-'+lokiNimi[4:6]
            df=df1[df1['Date'].str.startswith(filtteri)]
        else:
            filtteri='20'+lokiNimi[:2]+'-'+lokiNimi[2:4]
            df=df1[df1['Date'].str.startswith(filtteri)]

        tulo = df['Lammitys_tulo_index'] /10
        meno = df['Lammitys_meno_index'] /10
        kaivo_meno = df['Kaivo_meno_index'] /10
        kaivo_tulo =df['Kaivo_tulo_index'] /10
        ulko_lampo =df['Ulkolampotila_index'] /10
        kayttovesilampo =df['Kayttovesi_index'] /10
        tavoitearvot =df['Laskettu_meno_index'] /10
        asteminuutit =df['Asteminuutit_index'] /10

        fig,ax=plt.subplots(nrows=2,ncols=1,figsize=(20, 10), dpi=100)        
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
        plt.title(self.lokiNimi,fontsize=12, color="darkred", loc="center")
        image_nimi=self.lokiNimi.split('.')[0]  #.csv-liite pois
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