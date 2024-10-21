Raspberry Pi Based Oscilloscope


1. Hardware Configuration  - Circuit diagram
ADS1115 and Raspberry Pi Connections:
VDD – 3.3v
GND – GND
SDA – SDA
SCL – SCK

2. Installation of dependencies:

sudo apt-get install build-essential python-dev python-smbus git

git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git

cd Adafruit_Python_ADS1x15 
sudo python setup.py install

3. Test the installation

//Check examples directory
cd examples 
ls
//Check for simpletest.py
python simpletest.py


//Install the other packages used for graph
sudo apt-get install python3-matplotlib
sudo pip3 install drawnow

//Write the following code in python file

import time
import matplotlib.pyplot as plt
from drawnow import *
# Import the ADS1x15 module.
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val = [ ]
cnt = 0
plt.ion()

# Start continuous ADC conversions on channel 0 using the previous gain value.
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')


#create the figure function
def makeFig():
	plt.ylim(-5000,5000)
	plt.title('Osciloscope')
	plt.grid(True)
	plt.ylabel('ADC outputs')
	plt.plot(val, 'ro-', label='Channel 0')
	plt.legend(loc='lower right')

while (True):
# Read the last ADC conversion value and print it out.
	value = adc.get_last_result()
	print('Channel 0: {0}'.format(value))
	# Sleep for half a second.
	time.sleep(0.5)
	val.append(int(value))
	drawnow(makeFig)
	plt.pause(.000001)
	cnt = cnt+1
	if(cnt>50):
		val.pop(0)














