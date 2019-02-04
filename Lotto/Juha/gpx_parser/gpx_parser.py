import csv
import matplotlib.pyplot as plt
import pandas as pd  #csv kasittelyyn
import os
import smopy  #openstreetmap kaytto
import numpy as np
import glob


#  Ottaa gpx-fileen, tekee paikkapisteistä csv:n ja plotin openstreetmap taustalle
#
# tarvii seuraavat kirjastot (pip install kirjasto):
#    matplotlib, (pillow?), pandas, smopy
#
# to-do:
#   tsekkaa gpxpy
#
#################################################################################################
# dataformaatti:
# <?xml version="1.0" encoding="utf-8"?>
# <gpx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ...">
#  <metadata />
#  <trk>
#   <name>PK1</name>
#   <cmt />
#   <trkseg>
# 	<trkpt lat="60.4306755065918" lon="23.2658634185791">
#     <ele>59</ele>
#     <time>2018-04-27T14:25:17Z</time>
#    </trkpt>
#    <trkpt lat="60.4306755065918" lon="23.2658653259277">
#     <ele>59.2000007629394</ele>
#     <time>2018-04-27T14:25:18Z</time>
#    </trkpt>
####################################################################################################

def decode_aika(line):
    rivix=line.replace('<',',').replace('>',',').replace('-',',').replace('T',',').replace('Z',',').split(',')
    aika_output=[]
    temp=(rivix[4]),(rivix[3]),(rivix[2])
    paivays='.'.join(temp)
    aika_output.append(paivays)
    aika_output.append(rivix[5])
    return aika_output 

def decode_gpx(line):
    fields=line.replace('\"',',').split(',')
    #latitude
    lat_str=fields[1]
    #longitude
    lon_str=fields[3]
    return lat_str,lon_str

def tsekkaa_hakemistot(a,b,c):
    if not os.path.exists(a):
        os.makedirs(a)
    if not os.path.exists(b):
        os.makedirs(b)
    if not os.path.exists(c):
        os.makedirs(c)

def kirjoita_tiedostoon(file_nimi,otsikko,loppulista):
    with open('./csv/'+file_nimi, "w") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(otsikko)
        writer.writerows(loppulista)
    f.close()
        
def korjaa_csv_pilkut(file_nimi):  #jotta osaa avata exceliin suoraan
    with open('./csv/'+file_nimi, newline=None) as f:
        uusiTeksti=f.read()
    while ',' in uusiTeksti:
        uusiTeksti=uusiTeksti.replace(',',';')      
    with open('./csv/'+file_nimi, "w") as f:
        f.write(uusiTeksti)
    f.close()

def kasaa_loppulista(rivit):
    output=[]
    loppulista=[]
    count=0
    for i in range(len(rivit)):    
        if rivit[i].startswith('    <time>'):
            aika=decode_aika(rivit[i])
            output.insert(0,aika[1])
            output.insert(0,aika[0])
            loppulista.append(output)
            output=[]    
        elif rivit[i].startswith('   <trkpt'):
            lati,longi=decode_gpx(rivit[i])
            output.extend([lati])
            output.extend([longi])
            count+=1
        else:
            continue
    return loppulista    

def plottaa_lati_vs_longi(i_file_nimi,o_file_nimi):    
    df = pd.read_csv('./csv/'+o_file_nimi)
    latitudes = df['Latitude'] #you can also use df['column_name']
    longitudes =df['Longitude']

    latitudes=latitudes.iloc[latitudes.to_numpy().nonzero()] #nollat pois ennen laskelmaa
    longitudes=longitudes.iloc[longitudes.to_numpy().nonzero()]

    x_skaala_min=min(latitudes)
    x_skaala_max=max(latitudes)
    y_skaala_min=min(longitudes)
    y_skaala_max=max(longitudes)

    map = smopy.Map((x_skaala_min,y_skaala_min , x_skaala_max, y_skaala_max))
    #map = smopy.Map((60.425,23.26 , 60.435, 23.27), z=19)
    x, y = map.to_pixels(latitudes, longitudes)
    
    ax = map.show_mpl(figsize=(15,15),dpi=500) #
    ax.plot(x, y, 'or', ms=1, mew=1, alpha=0.4)    
    image_nimi=i_file_nimi.split('.')[0]  #.csv-liite pois
    plt.savefig('./kuvat/'+image_nimi, bbox_inches='tight')
    plt.show()

# ######## Main ##########
clear = lambda: os.system('cls')
clear()

print('Hakee gpx-fileestä ajan, latituden ja longituden, sekä plottaa kuvan lat vs lon')
print('File-sijainnit: gpx-hakemistossa input gpx, csv-hakemistoon tulostuu csv ja kuvat-hakemistoon png\n')

tsekkaa_hakemistot("gpx/","csv/","kuvat/")
fileet =glob.glob("gpx/*.gpx") #hakee hakemistossa olevat fileet
for i,n in enumerate(fileet):
    print('Hakemistosta löytyy: ',fileet[i].split('\\')[1])

input_file=input('\nAnna GPX-file-nimi (GPX-hakemistossa): ')
output_file='gpx_output.csv'
otsikko=[['Paivays','Aika','Latitude','Longitude']]

myFile=open('./gpx/'+input_file,mode='r') # luetaan gpx-file
rivit=list(myFile.readlines())

loppulista=kasaa_loppulista(rivit)
kirjoita_tiedostoon(output_file,otsikko,loppulista)
plottaa_lati_vs_longi(input_file,output_file)
korjaa_csv_pilkut(output_file)
