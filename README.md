#Home Alarm

A couple of python scripts which work together to detect if your door was opened.

Works with a Raspberry Pi B+, a magnetic door sensor and an Apple Mac Mini.

<img src="src="./home-alarm.JPG">

The sensor is connected to the GPIO Pin n°1 to send 3.3V and return to the n°18 Pin which check if there is voltage or not.

This detection is made by the alarm.py script.
If door is opened, the Pi send an alert to the script server.py

The python script server.py check if an alert was made by the pi.
If an alert is send, it launch an AppleScript which is able to run the “message” application and send an imessage or/and a sms to someone.

