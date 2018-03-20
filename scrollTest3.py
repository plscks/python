# scrolling text test 3
# OMG this is difficult maybe?
# written by plscks
#
#import time
#for i in range(10):
#    print('Update %d' % i, end='\r')
#    time.sleep(5)
import time

string = input('String to scroll: ')
for letter in string:
    print(' ' * 9 + letter, end='\r')
    time.sleep(2)
