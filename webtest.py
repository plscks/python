#!/usr/bin/python
# testing to see if I can tell if my website is up or down
# written by plscks
# References
# https://pinout.xyz/pinout/#https://pinout.xyz/pinout/#
#
# BCM 17 - blue LED website ALL GOOD
# BCM 22 - red LED website DOWN
# BCM 23 - white LED user connected to music stream ALL

import requests
import RPi.GPIO as GPIO
import urllib.request

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

site = 'http://plscks.ddns.net'
try:
    status = str(requests.head(site))
except:
    status = 'fail'
    pass

# This works, but when set to every minute blocks ssh which is no good
if status == str('<Response [200]>'):
    GPIO.output(17, 1) #Turn on blue LED
    GPIO.output(22, 0) #Make sure red LED is off
else:
    print(status)
    GPIO.output(22, 1) #Turn on red LED
    GPIO.output(17, 0) #Turn off blue LED

response = urllib.request.urlopen('http://localhost:8001')
html = response.read()
test = str(html)
linenumber = test.find("Listeners (current)")
streamnumber = linenumber + 49
listenernumber = test[streamnumber]
if int(listenernumber) > 0:
    GPIO.output(23, 1)
else:
    GPIO.output(23, 0)
