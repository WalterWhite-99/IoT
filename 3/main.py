from machine import Pin,time_pulse_us
from time import sleep

redLed = Pin(13,Pin.OUT)
yellowLed = Pin(14,Pin.OUT)
cyanLed = Pin(15,Pin.OUT)

trigger = Pin(7,Pin.OUT)
echo = Pin(6,Pin.OUT)

def measure():
    trigger.high()
    sleep(0.2)

    trigger.low()

    pulseDuration = time_pulse_us(echo,Pin.high)
    distance = pulseDuration * 0.0343 /2
    return distance

def main():
    while True:
        distance = measure()
        print("Distance : {:.2f}".format(distance))

        if distance < 130:
            cyanLed.on()
            sleep(0.5)
            cyanLed.off()
        elif distance >=130 and distance <= 260:
            yellowLed.on()
            sleep(0.4)
            yellowLed.off()
        else :
            redLed.on()
            sleep(0.2)
            redLed.off()


if __name__ == "__main__":
    main()