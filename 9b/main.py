from machine import Pin
from picozero import Servo
from time import sleep
from dht import DHT22

servo = Servo(18)
dht = DHT22(Pin(6))

while True:
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()

    print(f"Temp : {temp} and Humidity : {hum}")

    if temp < 20:
        servo.min()
        sleep(0.2)
    elif temp >= 20 and temp <=45:
        servo.mid()
        sleep(0.2)
    else:
        servo.max()
        sleep(0.2)

    