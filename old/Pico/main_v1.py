from display_lib import drawDisplay
from post_lib import post_data, connect_to_wifi
from dht_lib import getMeasurements
import time

upload_data = False

if upload_data:
    connect_to_wifi()

while True:
    
    temperature, humidity = getMeasurements()
    drawDisplay(" Temp", " " + str(temperature))

    if upload_data:
        data = '{"temperature":' + str(temperature) + ', "humidity":'+ str(humidity) + '}'
        post_data(data)

    
    time.sleep(1)