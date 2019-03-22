# coding=utf-8
#import urllib
import json
import time
from urllib.request import urlopen


READ_API_KEY='WYSG8YT18DUC1QIQ'
CHANNEL_ID= '218784'


while True:
    TS = urlopen('https://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s' % (CHANNEL_ID,READ_API_KEY))

    response = TS.read()
    data=json.loads(response)


    #a = data['created_at']
    #b = data['field1']
    #c = data['field2']
    #d = data['field3']
    #print (a + "    " + b + "    " + c + "    " + d)
    print(data)
    
    time.sleep(5)   

    TS.close()

#ch = thingspeak.Channel(218784, api_key='WYSG8YT18DUC1QIQ', fmt='json', timeout=None, server_url='https://api.thingspeak.com' )
#ch = thingspeak.Channel(9)
#print(ch.get)