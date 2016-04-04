#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Python Script that works with a Raspberry Pi b+, a magnetic door sensor and a mac mini.
# This part is made to run on the Raspberry Pi.

import socket
import time
import RPi.GPIO as GPIO

# set the GPIO in listening mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)

# params to contact the server
params = ('IP_OF THE SERVER_SCRIPT', NUM_OF THE_PORT_THE SERVER_LISTEN)
BUFFER_SIZE = 1024 # default
messages = [b'|1\n'] # the message sended is not important, the fact that datas is received is enough to trigger the alarm.

while 1:
		if GPIO.input(18): # if voltage is detected, sleep 1 second
			time.sleep(1)		
		else : # if voltage is not detected, print "open" on the stadard out and send alarm to server.py 
			print("open")
			for m in messages:
				s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect(params) # connect to server.py with params
				s.send(m) #send the alarm message
				s.close() #close the connexion
			time.sleep(120) # sleep 2 min before loop
