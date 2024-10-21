from machine import Pin
from time import sleep
from dht import DHT22

dht = DHT22(Pin(0))
redLed = Pin(11,Pin.OUT)
yellowLed = Pin(12,Pin.OUT)
purpleLed = Pin(13,Pin.OUT)

while True:
    dht.measure()

    temp = dht.temperature()
    hum = dht.humidity()

    print(f"Temperature is {temp} and Humidity is {hum}")
    
    if temp <= 20:
        purpleLed.on()
        sleep(0.6)
        purpleLed.off()
    elif temp >20 and temp < 45:
        yellowLed.on()
        sleep(0.4)
        yellowLed.off()
    else:
        redLed.on()
        sleep(0.2)
        redLed.off()

