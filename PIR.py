        
import RPi.GPIO as GPIO
import time

PIR = 9
LED = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(LED , GPIO.OUT)         #LED output pin

try:
	while True:
		i=GPIO.input(PIR)
		if i==0:                 #When output from motion sensor is LOW
			print "No intruders",i
			GPIO.output(LED, GPIO.LOW)  #Turn OFF LED
			time.sleep(0.1)
		elif i==1:               #When output from motion sensor is HIGH
			print "Intruder detected",i
			GPIO.output(LED, GPIO.HIGH)  #Turn ON LED
			time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.output(LED, GPIO.LOW)
    print("\nApplication stopped!")
