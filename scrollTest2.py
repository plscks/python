# Python 3 scrolling text in console
# Here we go again!
# written by plscks
#
# Is this a test?
# It has to be.....
#
# example from:
# https://codegolf.stackexchange.com/questions/58732/make-me-a-scrolling-marquee


import time;s=input()*80
while 1:print("\033[2J",end=s[:80],flush=1);s=s[1:]+s[0];time.sleep(.1)
