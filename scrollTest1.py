# Scroll test 1
# written by plscks
# status: failure, does not function as intended in python3
# Ugh, this works great after a little tweaking.
# Now to tweak it a little for production
#
# push the envelope, watch it bend.

import time
import sys

string = input('Enter string to scroll?: ')
scroll = str(string) + '                                        '
scrollFinal = scroll * 99
while 1:
    for i in range(180):
        print(scrollFinal[i:i+40], end='\r')
        sys.stdout.flush()
        time.sleep(0.1)
