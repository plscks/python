# A simple Raspberry pi 3 GPIO test
# Written by
# (except lines 5-13, these are from the RPi site raspberrypi.org/documentation/usage/python/more.md)
# plscks 
import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom

GPIO.setup(17, GPIO.OUT)  # set up pin 17
GPIO.setup(18, GPIO.OUT)  # set up pin 18

GPIO.output(17, 1)  # turn on pin 17
GPIO.output(18, 1)  # turn on pin 18
