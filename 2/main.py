from machine import Pin
from time import sleep

pins = [
    Pin(0,Pin.OUT),
    Pin(1,Pin.OUT),
    Pin(2,Pin.OUT),
    Pin(3,Pin.OUT),
    Pin(10,Pin.OUT),
    Pin(11,Pin.OUT),
    Pin(12,Pin.OUT)
]

blinks = [
    [0,1,1,1,1,1,1],
    [1,0,1,1,1,1,1],
    [1,1,0,1,1,1,1],
    [1,1,1,0,1,1,1],
    [1,1,1,1,0,1,1],
    [1,1,1,1,1,0,1],
    [1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1] 
]

while True:
    for x in range(len(blinks)):
        for y in range(len(pins)):
            pins[y].value(blinks[x][y])
        sleep(0.2)
    
    for x in reversed(range(len(blinks))):
        for y in reversed(range(len(pins))):
            pins[y].value(blinks[x][y])
        sleep(0.2)
