
# -*- coding: utf-8 -*-
# Code antibouncing
# for using a keypad with the Raspberry Pi


import RPi.GPIO as GPIO
import time
import os
import cv2

# camera init
video = cv2.VideoCapture("/dev/video0")
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
#

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

LED = 11	# rojo
LED2 =10	# amarillo
LED3 = 27	# blanco
PIR = 17


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

GPIO.setup(PIR, GPIO.IN)         # Read output from PIR motion sensor

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

Enter = False # entre aue permet de verifie si le motpasse est nickel
Mot = []	# permet d`ajouter le mot passe

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        while(GPIO.input(C1) == True):
            pass
        Mot.append(str(characters[0]))
        print(characters[0])
    if(GPIO.input(C2) == 1):
        while(GPIO.input(C2) == True):
            pass
        Mot.append(str(characters[1]))
        print(characters[1])
    if(GPIO.input(C3) == 1):
        while(GPIO.input(C3) == True):
            pass
        Mot.append(str(characters[2]))
        print(characters[2])
    if(GPIO.input(C4) == 1):
        while(GPIO.input(C4) == True):
            pass   
        print(characters[3])
	if characters[3] == "D":
		global Enter
		Enter = True
		print(Mot, len(Mot))
	GPIO.output(line, GPIO.LOW)

# Code pour mot de passe

def mdp():
	MDP = ['1','2','3','4']
	if(Mot == MDP):
		print("ok")
		LedON(LED)
	else:
		print('pas ok')
		blinc(LED2)
	global Enter
	Enter = False
	while len(Mot) != 0:
		Mot.pop()
	print(Mot)

#LED ON
def LedON(led):
	GPIO.output(led, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(led, GPIO.LOW)
	
#PIR
def funcPIR():
	i=GPIO.input(PIR)
	global camera
	global verification
	if i==0:                 #When output from motion sensor is LOW
		#print "No intruders",i
		GPIO.output(LED3, GPIO.LOW)  #Turn OFF LED
		time.sleep(0.1)
		camera = False
		verification = True
	elif i==1:               #When output from motion sensor is HIGH
		#print "Intruder detected",i
		GPIO.output(LED3, GPIO.HIGH)  #Turn ON LED
		time.sleep(0.1)
		camera = True


#LED blinking
def blinc(led):
	i=3
	while i!=0:
		LedON(led)
		i=i-1
		time.sleep(0.25)

#main
try:
	while True:
		readLine(L1, ["1","2","3","A"])
		readLine(L2, ["4","5","6","B"])
		readLine(L3, ["7","8","9","C"])
		readLine(L4, ["*","0","#","D"])
		time.sleep(0.1)
		funcPIR()
		if(Enter == True):
			mdp()
		elif(camera == True):
			while True:
				ret,frame= video.read()
				writer.write(frame)
				##cv2.imshow('frame', frame)
				funcPIR()
				if cv2.waitKey(1) & 0xFF == 27:
					break
		elif(camera == False and verification == True):
			verification = False
			video.release()
			writer.release()
			cv2.destroyAllWindows()
			
					

except KeyboardInterrupt:
	GPIO.output(LED, GPIO.LOW)
	GPIO.output(LED2, GPIO.LOW)
	GPIO.output(LED3, GPIO.LOW)
	print("\nApplication stopped!")


	
