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
import operator

class Log():
    def __init__(self,lokiNimi):
        self.lokiNimi=lokiNimi  #input log nimi, 160225-1.LOG
        self.lokiKuukausi=lokiNimi[:4] # 1602
        self.loppulista=[]
        self.output_file=''        
        
    def lue_logi(self, fileet):
        self.hoida_kuukausi(fileet) #yhdistää fileet yhdeksi logiksi
        if len(self.lokiNimi)==4:
            self.output_file =self.lokiKuukausi+'.csv'
            infile='./data/'+self.lokiNimi+'.LOG'
        else:
            self.output_file=self.lokiNimi[:-4]+'.csv'
            infile='./data/'+self.lokiKuukausi+'.log'
        myFile=open(infile,mode='r') # luetaan file
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
        ll=lines[1]
        lines = sorted(lines[1:])
        f.close()
        f = open('./data/'+self.lokiKuukausi+'.log',"w")
        f.write(ll)
        for line in lines:
            if not line.startswith("D"): #poistetaan muut kuin datarivit
                f.write(line)

    def pura_log(self,line):
        output,loppulista=[],[]
        count=0
        for i in range(len(line)):    
            fields=line[i].split('\t')
            fields[-1]=fields[-1].strip()
            loppulista.append(fields)
        return loppulista

    def kirjoita_tiedostoon(self, tiedosto='',rivit=''):
        if tiedosto=='':
            tiedosto =self.output_file
        
        o =self.loppulista[0] #otsikko
        o[3],o[5],o[6],o[7],o[8],o[9],o[10],o[17],o[18] =["Ulkolampotila_index","Lammitys_meno_index","Lammitys_tulo_index","Kaivo_tulo_index"
           ,"Kaivo_meno_index","Laskettu_meno_index","Asteminuutit_index","Toimintatila_index","Kayttovesi_index"]

        if len(self.lokiNimi)>4:
            temp=[o]
            for i in self.loppulista[1:]:
                if i[0]==('20'+self.lokiNimi[:2]+'-'+self.lokiNimi[2:4]+'-'+self.lokiNimi[4:6]):
                    temp.append(i)
            self.loppulista=temp   
        
        with open('./csv/'+tiedosto, "w") as f:
            writer = csv.writer(f, lineterminator='\n', delimiter =';')
            writer.writerows(self.loppulista)
        f.close()

    def plottaa(self,lokiNimi):
        df1 = pd.read_csv('./csv/'+self.output_file, delimiter =';')
        if len(self.lokiNimi) !=4: #annettu päivä
            filtteri='20'+lokiNimi[:2]+'-'+lokiNimi[2:4]+'-'+lokiNimi[4:6]
            df=df1[df1['Date'].str.startswith(filtteri)]
        else: #  annettu kuukausi
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
        aika=pd.to_datetime(df.Time).dt.time
        
        fig,ax=plt.subplots(nrows=2,ncols=1,figsize=(20, 10), dpi=100)        
        ax0_plotit=[tulo,meno,kayttovesilampo,tavoitearvot]
        for i in range(4):
            if len(self.lokiNimi)==4:
                ax[0].plot(ax0_plotit[i],label=["Lämmitys tulo","Lämmitys meno","Käyttövesi","Tavoitearvot"][i], lw=1)
            else:
                ax[0].plot(aika,ax0_plotit[i],label=["Lämmitys tulo","Lämmitys meno","Käyttövesi","Tavoitearvot"][i], lw=1)
        ax[0].legend(fontsize=10, loc="best")
        plt.ylabel("Asteita", fontsize=10)
        ax[0].set_title(self.lokiNimi,fontsize=20,color="darkred",fontstyle='italic')
        ax[0].set_ylabel("Asteita", fontsize=10) 
        ax[0].set_xlabel("Aika", fontsize=10)   
        ax[0],ax[1].grid(True, which='major',color ="black",linestyle=':', linewidth=0.3)
        ax[1].plot(kaivo_tulo,label="Kaivo meno", lw=1)
        ax[1].plot(kaivo_meno,label="Kaivo tulo", lw=1)
        ax[1].plot(ulko_lampo,label="Ulkolämpö", lw=1)
        ax2=ax[1].twinx()
        ax2.plot(asteminuutit, label="Asteminuutit", c="black",lw=1)
        ax[1].legend(fontsize=10, loc="upper left")
        ax[0].legend(fontsize=10, loc="best")
        ax2.legend(fontsize=10, loc="best")
        
        image_nimi=self.lokiNimi.split('.')[0]  #.csv-liite pois
        plt.savefig('./kuvat/'+image_nimi, bbox_inches='tight')
        plt.tight_layout() 
        plt.show()
