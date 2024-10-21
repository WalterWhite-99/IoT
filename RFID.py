// RFID Configuration with Raspberry Pi

1. Make following connections:

SDA connects to Pin 24.
SCK connects to Pin 23.
MOSI connects to Pin 19.
MISO connects to Pin 21.
RST connects to Pin 22.

GND connects to Pin 6.
3.3v connects to Pin 1.


2. Check Serial interface is enabled or not
Go to Raspi-Config - Interface - Serial
If it is disabled - make it enable and reboot the system

3.Give following command on terminal to check serail connection is 
enabled or not

lsmod | grep spi

//Should get pi_bcm2835 as a result

4. Install following packages
sudo pip3 install spidev
sudo pip3 install mfrc522

5. Make directory for keeping all scripts
mkdir ~/pi-rfid151

Save following code in Write.py


import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()


//Write following code in Read.py

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
	if(text==”user1”)
		//on green led
	Else
		//on red led
finally:
        GPIO.cleanup()





