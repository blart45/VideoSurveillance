

# This program allows a user to enter a
# Code. If the C-Button is pressed on the
# keypad, the input is reset. If the user
# hits the A-Button, the input is checked.

import RPi.GPIO as GPIO
import time

# These are the GPIO pin numbers where the
# lines of the keypad matrix are connected
L1 = 26
L2 = 17
L3 = 27
L4 = 22

# These are the four columns
C1 = 5
C2 = 6
C3 = 16
C4 = 13
# GPIO setup and imports omitted

def readLine(line, characters):
	GPIO.output(line, GPIO.HIGH)
	if(GPIO.input(C1) == 1):
    	    print(characters[0])
	if(GPIO.input(C2) == 1):
        	    print(characters[1])
	if(GPIO.input(C3) == 1):
    	    print(characters[2])
	if(GPIO.input(C4) == 1):
    	    print(characters[3])
	GPIO.output(line, GPIO.LOW)

try:
	while True:
    	    readLine(L1, ["1","2","3","A"])
    	    readLine(L2, ["4","5","6","B"])
    	    readLine(L3, ["7","8","9","C"])
    	    readLine(L4, ["*","0","#","D"])
    	    time.sleep(0.1)
except KeyboardInterrupt:
	print("\nApplication stopped!")
