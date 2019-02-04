import csv
import os
import matplotlib.pyplot as plt
import pandas as pd  #csv kasittelyyn
import smopy  #openstreetmap kaytto
import numpy as np
import glob
clear = lambda: os.system('cls')
clear()

# to:do
#  azimut ja elevation. Mitä muuta lisäksi ?
# www.gpsinformation.org/dale/nmea.htm
##############################################################################################################################
# NMEA parser
# tekee nmea txt input fileesta csv fileen, missä tarvittava data#
#dataformaatti:
#   $GPGGA  current fix data, 3D &accuracy.
#    120404.000,6023.3745,N,02306.1779,E,1,6,1.69,35.7,M,20.3,M, ,*6A
#       12:04:04 UTC 
#       lati 60deg23.3745'N 
#       longi 23deg06.1179'E 
#       fix qual 0-8 
#       no. satellites 
#       hor. dilut of posit. 
#       altitude m 
#       height of geoid
#       time since dgps update 
#       checksum      
#   $GPGSA  satellite status data
#   $GPGSV  
#    3,1,10,23,72, 201,42,03,54,129,40,09,45,232,39,06,45,289,15*76
#       no. sentences 
#       sent 1 of3 
#       no. satellites in view 
#       satellite PRN 
#       elevation deg 
#       azimuth deg 
#       snr, ja 3 muuta lukua(mitä?), 4 satelliittia jonossa      
#       checksum (*76)
#   $GPRMC  minimum gps sentences
##############################################################################################################################

def decode_gga(line):
    fields=line.split(',')
    for i,e in enumerate(fields):
        if fields[i]=='':
            fields[i]='0'  
    time_string=fields[1]
    hour=int(time_string[:2])
    minute=int(time_string[2:4])
    sec=int(time_string[4:6])
    aika=(str(hour)+':'+str(minute)+':'+str(sec))

    #latitude
    lat_str=fields[2]
    if lat_str !='0':
        y=int(lat_str[:2])+float(lat_str[2:])/60
        if fields[3]=='S':
            y=-y
        y=round(y,5)
    else:
        y='0'

    #longitude
    lon_str=fields[4]
    if lon_str !='0':
        x=int(lon_str[:3])+float(lon_str[3:])/60
        if fields[5]=='W':
            x=-x
        x=round(x,5)
    else:
        x='0'
    return aika,y,x

def pura_nmea(line):
    output=[]
    count=0
    loppulista=[]
    for i in range(len(rivit)):    
        if line[i].startswith('$GPGGA'):
            aika,lati,longi=decode_gga(line[i])
            output.extend([aika,lati,longi])
            count+=1

        elif line[i].startswith('$GPGSV'):
            gsv_output,r=decode_gsv(line[i]) 
            output.extend(gsv_output)
            if r=='3':
                loppulista.append(output)
                output=[]
        else:
            continue
    return loppulista

def decode_gsv(line):
    rivix=line.split(',')
    gsv_output=[]
    if (rivix[2])=='1':
        #gsv_output.extend([(rivix[7]),(rivix[11]),(rivix[15]),(rivix[19][:2])])
        gsv_output.extend([(rivix[5]),(rivix[6]),(rivix[7]),(rivix[11]),(rivix[15]),(rivix[19][:2])])
    elif rivix[2]=='2':
        gsv_output.extend([(rivix[7]),(rivix[11]),(rivix[15]),(rivix[19][:2])])
    else:
        gsv_output.extend([(rivix[7])])
    return gsv_output,rivix[2] 

#Onko hakemistot jo olemassa, jos ei niin luodaan
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

def siivoa_listaa(loppulista):
    y=[]
    for i in (loppulista):
        for n,e in enumerate(i): # korvataan tyhjät nollalla, ja lopun checksum probleema *
            if e=='' or ('*' in str(e)):
                i[n]='0'
            if n>2:
                i[n]=int(i[n])
        y=i[0].split(':')
        if len(y[0])==1:  #aikaan 2digit tunneille, minuuteille ja sekunneille
            y[0]='0'+y[0]
        if len(y[1])==1:
            y[1]='0'+y[1]
        if len(y[2])==1:
            y[2]='0'+y[2]
        y=':'.join(y)
        i[0]=y
        #print(i)
    return loppulista

#Jotta suomi-excel osaa avata  suoraan        
def korjaa_csv_pilkut(file_nimi):  
    with open('./csv/'+file_nimi, newline=None) as f:
        uusiTeksti=f.read()
    while ',' in uusiTeksti:
        uusiTeksti=uusiTeksti.replace(',',';')        
    with open('./csv/'+file_nimi, "w") as f:
        f.write(uusiTeksti)
    f.close()

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

######## Main ##########
clear = lambda: os.system('cls')
clear()

print('Hakee nmea-fileestä ajan, latituden, longituden, elvationin ja Azimuthin, sekä plottaa kuvan lat vs lon')
print('File-sijainnit: nmea-hakemistossa input txt, csv-hakemistoon tulostuu csv ja kuvat-hakemistoon png\n')

tsekkaa_hakemistot("nmea/","csv/","kuvat/") #onko jo olemassa, jos ei niin luodaan
fileet =glob.glob("nmea/*.txt") #hakee hakemistossa olevat fileet
for i,n in enumerate(fileet):
    print('Hakemistosta löytyy: ',fileet[i].split('\\')[1])

input_file=input('Anna NMEA-tekstifile-nimi (samassa hakemistossa): ')
output_file='csv_output.csv'
otsikko=[['Aika','Latitude','Longitude','Elevation','Azimuth','Sat1 SNR','Sat2 SNR','Sat3 SNR','Sat4 SNR','Sat5 SNR','Sat6 SNR','Sat7 SNR','Sat8 SNR', 'Sat9 SNR']]

myFile=open('./nmea/'+input_file,mode='r') # luetaan nmea-file
rivit=list(myFile.readlines())

loppulista=[]
loppulista=pura_nmea(rivit)
loppulista=siivoa_listaa(loppulista)
kirjoita_tiedostoon(output_file,otsikko,loppulista)
plottaa_lati_vs_longi(input_file,output_file)
korjaa_csv_pilkut(output_file)