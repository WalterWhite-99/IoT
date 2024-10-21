1. Open telegram app on mobile phone
2. Search Botfather
3. give following command for creating new bot
	/newbot
4. Provide unique name for your bot
5. Provide the unique user name for your bot

Raspberry pi
Give following command on terminal
1. Check whether your device is connected to internet or not 
2. sudo pip3 install telepot
3. Type following code in Python
4. Check the code for syntax error
5. Run the code
6. Open telegram on mobile phone
7. Search for new bot created and start with new bot
8. Give on and off command from telegram which will 
switch on and switch off the LED connected to Raspberry Pi


import sys
import time
import telepot
import RPi.GPIO as GPIO
from telepot.loop import MessageLoop

def on(pin):
	GPIO.output(pin,GPIO.HIGH)
	return

def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20,0)   #off Initially

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)
    
    #Extra from yt
    if 'on' in command:
        GPIO.output(20,1) # on Led
    if 'off' in command:
        GPIO.output(20,0) #off Led
    message = "something happened"
    bot.sendMessage(chat_id,message)
    
    if command == '/on':
       bot.sendMessage(chat_id, on(20))
    elif command =='/off':
       bot.sendMessage(chat_id, off(20))

bot = telepot.Bot('Your token')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
    
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()
	finally:
        print('Test')




