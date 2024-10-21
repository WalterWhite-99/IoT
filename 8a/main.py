from machine import Pin
from time import sleep
from dht import DHT22

dht = DHT22(Pin(0)) 

while True:
    dht.measure()

    temp = dht.temperature()
    hum = dht.humidity()

    print(f"Temperature is {temp} and Humidity is {hum}")
    sleep(0.5)