#! /usr/bin/env python

import time
import RPi.GPIO as GPIO
import smtplib

GPIO.setup(18, GPIO.IN)

while 1:

	if GPIO.input(18):
		time.sleep(1)		
	else : 
	
		server = smtplib.SMTP('SMTP OF YOUR MAIL PROVIDER' , 587)
		server.starttls()
		server.login("YOUR MAIL ADRESS" , "PASSWORD OF YOUR MAIL")
		msg = "MESSAGE YOU WANT TO SEND"
		server.sendmail("MAIL_FORM" , "MAIL_TO" , msg)
		server.quit()
		time.sleep(120)

	time.sleep(1)

