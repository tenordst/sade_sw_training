import sys
import csv
import locale
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from os import system, name 

class Summaa():
    def __init__(self,lokiNimi):
        self.lokiNimi=lokiNimi
        self.lokiKuukausi=lokiNimi[:4]
        self.loppulista=[]
        self.output_file=''
        self.kaynnistyksia=''    
        self.lisalampo=''     

    def laskeJaPrinttaa(self):        
        if len(self.lokiNimi) !=4: #annettu päivä
            self.output_file=self.lokiNimi[:-4]+'.csv' #.split('.')[0] +'.csv'
            filtteri='20'+self.lokiNimi[:2]+'-'+self.lokiNimi[2:4]+'-'+self.lokiNimi[4:6]
            df1 = pd.read_csv('./csv/'+self.output_file)
            df=df1[df1['Date'].str.startswith(filtteri)] 
            paiva =df.iloc[1][0]         
        else: #  annettu kuukausi
            self.output_file=self.lokiNimi+'.csv' #.split('.')[0] +'.csv'
            filtteri='20'+self.lokiNimi[:2]+'-'+self.lokiNimi[2:4]
            df1 = pd.read_csv('./csv/'+self.output_file)
            df=df1[df1['Date'].str.startswith(filtteri)]
            paiva =df.iloc[1][0][:7]
            
        kaivo_meno_raja = 2 # 0.2C
        lisalampo_raja = -400
        pumppu_kaynnistyy = -60
        pumppu_pysahtyy = 0
        kaynnistyksia=0
        lisalampo=0
        for index, row in df.iterrows():
            if df.iloc[index]['Toimintatila_index'] >10 and df.iloc[index-1]['Toimintatila_index'] ==10:
                kaynnistyksia +=1
            if df.iloc[index]['Asteminuutit_index']/10 <lisalampo_raja:
                lisalampo+=1
        self.kaynnistyksia=kaynnistyksia
        self.lisalampo=lisalampo
        self.paiva=paiva
        self.kaynnistyksia=kaynnistyksia
        self.mittauksia=len(df.index)
        self.pieninAsteminuutti=df['Asteminuutit_index'].min()/10
        self.kaynnissaKokoajastaLammitys=round(100*(len(df[df['Toimintatila_index'].isin([30])])/len(df.index)),2)
        self.kaynnissaKokoajastaVesi=round(100*(len(df[df['Toimintatila_index'].isin([20])])/len(df.index)),2)
        self.keskimenolampo=round((df['Lammitys_meno_index'].sum()/10)/len(df.index),2)
        self.keskitulolampo=round((df['Lammitys_tulo_index'].sum()/10)/len(df.index),2)
        self.pieninkaivonTulo=df['Kaivo_tulo_index'].min()/10
        self.pieninkaivonMeno=df['Kaivo_meno_index'].min()/10
        self.keskiulkolampotila=round((df['Ulkolampotila_index'].sum()/10)/len(df.index),2)

        print('\nPäivämäärä/kuukausi:\t\t\t', self.paiva)
        print('Käynnistyksiä:\t\t\t\t', self.kaynnistyksia)
        print ('Mittauksia:\t\t\t\t', self.mittauksia)
        print('Pienin asteminuutti:\t\t\t', self.pieninAsteminuutti)
        print('Kaynnissä kokonaisajasta (lammitys):\t',self.kaynnissaKokoajastaLammitys,'%')
        print('Kaynnissä kokonaisajasta (vesi):\t',self.kaynnissaKokoajastaVesi,'%')
        print('Lisälämpö päällä:\t\t\t', self.lisalampo)
        print('Keskimenolämpötila:\t\t\t',self.keskimenolampo)
        print('Keskitulolämpötila:\t\t\t',self.keskitulolampo)
        print('Pienin kaivon tulolampo:\t\t' ,self.pieninkaivonTulo )      
        print('Pienin kaivon menolampo:\t\t' ,self.pieninkaivonMeno )    
        print('Keskiulkolampotila:\t\t\t',self.keskiulkolampotila,'\n')
    
    def tulostaSummary(self):
        #with open('./csv/'+'summary'+self.lokiNimi[:-4]+'.csv', "w") as f:
        a=[['Päivä','Käynnistyksiä','Mittauksia','Pienin asteminuutti','Käynnissä kokonaisajasta (lämmitys)', 'Käynnissä kokonaisajasta (vesi)', 'Lisälämpö päällä', 'Keskimenolämpötila','Keskitulolämpötila', 'Pienin kaivon tulolämpö','Pienin kaivon menolämpö', 'Keskiulkolämpötila']]
        b=[[self.paiva,self.kaynnistyksia,self.mittauksia,self.pieninAsteminuutti,self.kaynnissaKokoajastaLammitys,self.kaynnissaKokoajastaVesi,self.lisalampo,self.keskimenolampo,self.keskitulolampo,self.pieninkaivonTulo,self.pieninkaivonMeno,self.keskiulkolampotila]]
        if len(self.lokiNimi)==4:filee= self.lokiNimi
        else:filee=self.lokiNimi[:-4]
        with open('./csv/'+'summary'+filee+'.csv','w') as resultFile:
            wr = csv.writer(resultFile, dialect='excel')
            wr.writerows(a)
            wr.writerows(b)

    def korjaa_csv_pilkut(self):  
        if len(self.lokiNimi)==4:filee= self.lokiNimi
        else:filee=self.lokiNimi[:-4]
        with open('./csv/'+'summary'+filee+'.csv', newline=None) as f:
            uusiTeksti=f.read()
        while ',' in uusiTeksti:
            uusiTeksti=uusiTeksti.replace(',',';')        
        with open('./csv/'+'summary'+filee+'.csv', "w") as f:
            f.write(uusiTeksti)
        f.close()


