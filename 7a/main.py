from machine import Pin,I2C
from time import sleep
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)

I2cAddr = i2c.scan()[0]

lcd = I2cLcd(i2c,I2cAddr,2,16)

def main():
    while True:
        lcd.putstr("Vrushabh")
        sleep(0.5)
        lcd.clear()
        sleep(0.5)


if __name__ == "__main__":
    main()