from machine import Pin,I2C
from time import sleep
from pico_i2c_lcd import I2cLcd
from dht import DHT22

dht = DHT22(Pin(6))

i2c = I2C(0,sda = Pin(0), scl = Pin(1), freq = 400000)

i2c_addr = i2c.scan()[0]

lcd = I2cLcd(i2c,i2c_addr,2,16)

while True:
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()

    lcd.putstr("Temp : {0}".format(temp))
    sleep(0.5)
    lcd.clear()

    lcd.putstr("Humidity : {0}".format(hum))
    sleep(0.5)
    lcd.clear()