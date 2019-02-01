import csv
import os
clear = lambda: os.system('cls')
clear()
# to:do
#  azimut ja elevation. Mitä muuta lisäksi ?
# www.gpsinformation.org/dale/nmea.htm
##############################################################################################################################
# NMEA parser
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
        y=round(y,4)
    else:
        y='0'

    #longitude
    lon_str=fields[4]
    if lon_str !='0':
        x=int(lon_str[:3])+float(lon_str[3:])/60
        if fields[5]=='W':
            x=-x
        x=round(x,4)
    else:
        x='0'
    return aika,y,x

def decode_gsv(line):
    rivix=list(line.split(','))
    gsv_output=[]
    if (rivix[2])=='1':
        gsv_output.extend([(rivix[7]),(rivix[11]),(rivix[15]),(rivix[19][:2])])
    elif rivix[2]=='2':
        gsv_output.extend([(rivix[7]),(rivix[11]),(rivix[15]),(rivix[19][:2])])
    else:
        gsv_output.extend([(rivix[7])])


    return gsv_output,rivix[2] 
def siivoa_listaa(loppulista):
    y=[]
    for i in (loppulista):
        for n,e in enumerate(i):
            if e=='' or ('*' in str(e)):
                i[n]='0'
            if n>2:
                i[n]=int(i[n])
        y=i[0].split(':')
        if len(y[0])==1:
            y[0]='0'+y[0]
        if len(y[1])==1:
            y[1]='0'+y[1]
        if len(y[2])==1:
            y[2]='0'+y[2]
        y=':'.join(y)
        i[0]=y
        #print(i)
    return loppulista

def kirjoita_tiedostoon(file_nimi,otsikko,loppulista):
    with open(file_nimi, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(otsikko)
        writer.writerows(loppulista)
        output.close()
        
def korjaa_csv_pilkut(file_nimi):
    with open(file_nimi, newline=None) as f:
        uusiTeksti=f.read()
    while ',' in uusiTeksti:
        uusiTeksti=uusiTeksti.replace(',',';')        
    with open(file_nimi, "w") as f:
        f.write(uusiTeksti)
    f.close()



######## main ##########
input_file=input('Anna NMEA-tekstifile-nimi (samassa hakemistossa): ')
output_file='csv_output.csv'

myFile=open(input_file,mode='r')
rivi=list(myFile.readlines())

output=[]
loppulista=[]
count=0

for i in range(len(rivi)):    
    if rivi[i].startswith('$GPGGA'):
        aika,lati,longi=decode_gga(rivi[i])
        output.extend([aika,lati,longi])
        count+=1

    elif rivi[i].startswith('$GPGSV'):
        gsv_output,r=decode_gsv(rivi[i]) 
        output.extend(gsv_output)
        if r=='3':
            loppulista.append(output)
            output=[]
    else:
        continue

otsikko=[['Aika','Latitude','Longitude','Sat1 SNR','Sat2 SNR','Sat3 SNR','Sat4 SNR','Sat5 SNR','Sat6 SNR','Sat7 SNR','Sat8 SNR', 'Sat9 SNR']]
loppulista=siivoa_listaa(loppulista)
kirjoita_tiedostoon(output_file,otsikko,loppulista)
korjaa_csv_pilkut(output_file)
