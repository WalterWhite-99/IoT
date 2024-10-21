from machine import Pin, I2C, time_pulse_us
from time import sleep
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)

i2c_Addr = i2c.scan()[0]

lcd = I2cLcd(i2c,i2c_Addr,2,16)

echo = Pin(6,Pin.OUT)
trigger = Pin(7,Pin.OUT)

def measure():
    trigger.high()
    sleep(0.2)
    trigger.low()

    pulseDuration = time_pulse_us(echo,Pin.high)
    distance = pulseDuration * 0.0343 / 2

    return distance

while True:
    distance = measure()
    lcd.putstr("Distance:{:.2f}".format(distance))
    print("Distance:{:.2f}".format(distance))
    sleep(0.5)
    lcd.clear()
    sleep(0.2)