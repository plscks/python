#!/usr/bin/python
# testing to see if I can tell if my website is up or down
# written by plscks
# References
# https://pinout.xyz/pinout/#https://pinout.xyz/pinout/#
#
# BCM 17 - blue LED website ALL GOOD
# BCM 22 - red LED website DOWN
# BCM 23 - white LED music stream ALL GOOD

import requests
import RPi.GPIO as GPIO

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


if status == str('<Response [200]>'):
#    print(site + ' is okay right now')
    GPIO.output(17, 1) #Turn on blue LED
    GPIO.output(22, 0) #Make sure red LED is off
#    GPIO.cleanup()
else:
#    print(site + ' is busted!! TRIGGER THE ALARMS!')
    print(status)
    GPIO.output(22, 1) #Turn on red LED
    GPIO.output(17, 0) #Turn off blue LED
#    GPIO.cleanup()
