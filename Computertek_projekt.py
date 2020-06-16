import time
from grovepi import *
import math

# Grove Relay @ D4
relay = 4
# Grove Temp @ D7
sensor = 7

pinMode(relay,"OUTPUT")

blue = 0
#white = 1 

while True:
    try:
        [temp,humidity] = dht(sensor,blue)
        
        if math.isnan(temp) == False:
            print(temp)
            if float(temp) > 28.0:
                digitalWrite(relay,1)
            else:
                digitalWrite(relay,0)

    except IOError:
        print ("Error")