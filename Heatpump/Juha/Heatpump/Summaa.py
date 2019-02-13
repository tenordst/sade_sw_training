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
            df1 = pd.read_csv('./csv/'+self.output_file,delimiter =';')
            df=df1[df1['Date'].str.startswith(filtteri)] 
            paiva =df.iloc[1][0]         
        else: #  annettu kuukausi
            self.output_file=self.lokiNimi+'.csv' #.split('.')[0] +'.csv'
            filtteri='20'+self.lokiNimi[:2]+'-'+self.lokiNimi[2:4]
            df1 = pd.read_csv('./csv/'+self.output_file, delimiter =';')
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
        a=[['Paiva','Kaynnistyksia','Mittauksia','Pienin asteminuutti','Kaynnissa kokonaisajasta (lammitys)', 'Kaynnissa kokonaisajasta (vesi)'
            ,'Lisalampo paalla', 'Keskimenolampotila','Keskitulolampotila', 'Pienin kaivon tulolampo','Pienin kaivon menolampo', 'Keskiulkolampotila']]
        b=[[self.paiva,self.kaynnistyksia,self.mittauksia,self.pieninAsteminuutti,self.kaynnissaKokoajastaLammitys,self.kaynnissaKokoajastaVesi
            ,self.lisalampo,self.keskimenolampo,self.keskitulolampo,self.pieninkaivonTulo,self.pieninkaivonMeno,self.keskiulkolampotila]]
        if len(self.lokiNimi)==4:filee= self.lokiNimi[:2]
        else:filee=self.lokiNimi[:-8]
        outfile='./csv/'+'summary'+filee+'.csv'
        if os.path.isfile(outfile):
            mukana=0
            df = pd.read_csv(outfile,delimiter =';',engine='python')
            for index,i in df.iterrows():
                if df.iloc[index]['Paiva']==self.paiva:
                    mukana = 1 
            if mukana!=1:
                with open(outfile,'a',newline="\n") as resultFile:
                    wr = csv.writer(resultFile, dialect='excel', delimiter =';')
                    wr.writerows(b)
                df = pd.read_csv(outfile,delimiter =';',engine='python')
                df =df.sort_values(["Paiva"])
                df.to_csv(outfile, sep=';',encoding='utf-8', index=False)
        else:
            with open(outfile,'w',newline="\n") as resultFile:
                wr = csv.writer(resultFile, dialect='excel', delimiter =';')
                wr.writerows(a)
                wr.writerows(b)
        self.plottaa(outfile)
        
    def plottaa(self,outfile):
        df = pd.read_csv(outfile, delimiter =';')
        p = df['Paiva']
        k= df['Kaynnistyksia']
        m = df['Mittauksia']
        p=df['Pienin asteminuutti'] 
        kkl =df['Kaynnissa kokonaisajasta (lammitys)']
        kkv =df['Kaynnissa kokonaisajasta (vesi)']
        l=df['Lisalampo paalla']
        kml=df['Keskimenolampotila']
        ktl=df['Keskitulolampotila']
        pktl=df['Pienin kaivon tulolampo']
        pkml=df['Pienin kaivon menolampo']
        kul=df['Keskiulkolampotila']

        fig,ax=plt.subplots(nrows=2,ncols=1,figsize=(20, 10), dpi=100)        
        ax0_plotit=[pktl,pkml,kul,l]
        for i in range(4):
            ax[0].plot(ax0_plotit[i],label=["Pienin kaivon tulolampo","Pienin kaivon menolampo","Keskiulkolampotila","Lisalampo paalla"][i], lw=1)

        ax[0].legend(fontsize=10, loc="upper left")
        plt.ylabel("Asteita", fontsize=10)
        ax[0].set_xlabel("Paivä/kk", fontsize=10)   
        ax[0],ax[1].grid(True, which='major',color ="black",linestyle=':', linewidth=0.3)
      
        ax[1].plot(kkl,label="Käynnissä kokoajasta (läm)", lw=1)
        ax[1].plot(kkv,label="Käynnissä kokoajasta (vesi)", lw=1)
        ax[1].plot(kml,label="Keskimenolämpötila", lw=1)
        ax[1].plot(ktl,label="Keskitulolämpötila", lw=1)
        ax1=ax[1].twinx()
        ax1.plot(p, label="Pienin asteminuutti", c="black",lw=1)  
        ax[1].legend(fontsize=10, loc="upper left")
        ax1.legend(fontsize=10, loc="upper right")
       
        image_nimi='./kuvat/summary'+self.lokiKuukausi[:2]+'.png'
        plt.savefig(image_nimi, bbox_inches='tight')
        plt.tight_layout() 
        plt.show()
