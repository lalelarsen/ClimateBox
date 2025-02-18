import dht
import machine

# Set up the DHT22 sensor
dht_pin = machine.Pin(2)  # GPIO pin where the DHT22 is connected (change according to your setup)
sensor = dht.DHT22(dht_pin)

def setPin(pin):
    dht_pin = pin
    sensor = dht.DHT22(pin)

def getMeasurements():
    sensor.measure()
    temperature = sensor.temperature()  # In Celsius
    humidity = sensor.humidity()  # In percentage
    
    return temperature, humidity
