# -*- coding: utf-8 -*-
# Code antibouncing
# for using a keypad with the Raspberry Pi


import RPi.GPIO as GPIO
import time

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

Enter = False 
Mot = []

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
	else:
		print('pas ok')
	global Enter
	Enter = False
	while len(Mot) != 0:
		Mot.pop()
	print(Mot)
	


#main

try:
    while True:
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)
        
        if(Enter == True):
			mdp()
        
        
except KeyboardInterrupt:
    print("\nApplication stopped!")
	
