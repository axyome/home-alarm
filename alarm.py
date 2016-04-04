#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)


params = ('IP_OF THE SERVER_SCRIPT', NUM_OF THE_PORT_THE SERVER_LISTEN)
BUFFER_SIZE = 1024 # default
messages = [b'|1\n']

while 1:
		if GPIO.input(18):
			time.sleep(1)		
		else : 
			print("open")
			for m in messages:
				s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect(params)
				s.send(m)
				s.close()
			time.sleep(120)
