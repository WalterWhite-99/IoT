from time import sleep
from picozero import Servo

servo = Servo(18)

while True:
    servo.min()
    sleep(0.5)

    servo.mid()
    sleep(0.5)

    servo.max()
    sleep(0.5)