# Scroll test 1
# written by plscks
# status: failure, does not function as intended in python3

import time,sys

s=input('Enter string to scroll: ')
while 1:
    for i in range(80):
        print(s[i:i+80])
        sys.stdout.flush()
        time.sleep(0.1)
