#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Python Script that works with a Raspberry Pi b+, a magnetic door sensor and a mac mini.
# This part is made to run on the Apple Mac Mini.

import socketserver
import time
import os

# PARAMS OF THE SCRIPT.
# set the params to the IP of the Mac Mini and select a port your python alarm server will listen.
# the var bashcmd contains the command to run in bash on the Mac Mini to send imessage
# the var bashcmd2 contains the command to run in bash on the Mac Mini to send sms
# to send sms, a redirect in apple products must be set between mac mini and an iphone.

params = ('IP_TO LISTEN', NUM_OF_THE_PORT_TO_LISTEN)
bashcmd = "osascript PATH_OF_THE_APPLESCRIPT ADRESS_FOR_IMESSAGE 'TEXT_TO_SEND_BY_IMESSAGE' "
bashcmd2 = "osascript PATH_OF_THE_APPLESCRIPT PHONENUMBER_FOR_SMS 'TEXT_TO_SEND_BY_SMS' "

class ExampleTCPHandler(socketserver.StreamRequestHandler):
	def handle(self):
                self.data = self.rfile.readline().strip()
                print("ALARME DECLENCHEE LE "+time.strftime('%d/%m/%y à %H:%M', time.localtime()))
                os.system(bashcmd)
                os.system(bashcmd2)
if __name__ == '__main__':
	server = socketserver.TCPServer(params, ExampleTCPHandler)
	server.serve_forever()

