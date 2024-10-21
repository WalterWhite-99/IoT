from machine import Pin
from time import sleep

led1 = Pin(0,Pin.OUT)
led2 = Pin(2,Pin.OUT)
led3 = Pin(5,Pin.OUT)
led4 = Pin(9,Pin.OUT)

arr = [led1,led2,led3,led4]

while True:
    for x in arr:
        x.on()
        sleep(0.4)

    for x in reversed(arr):
        x.off()
        sleep(0.2)

    for x in arr:
        x.on()
        
    sleep(0.5)
    for y in reversed(arr):
        y.off()
        sleep(0.1)