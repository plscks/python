#!/usr/bin/python
# Version 1
## Show menu ##
import os
import time


def new():
    ROnumber = input('RO Number: ')
    with open(ROnumber, 'wt') as f:
        f.write('RO number: ')
        f.write(ROnumber)
        f.write('\n')
    quit()

print (30 * '-')
print ('   M A I N - M E N U')
print (30 * '-')
print ('1. New RO')
print ('2. Existing RO')
print ('3. Quit')
print (30 * '-')

## Get input ###
choice = input('Enter your choice [1-3] : ')

### Convert string to int type ##
choice = int(choice)

### Take action as per selected menu-option ###
if choice == 1:
    print ('Opening new RO...')
    time.sleep(2)
    os.system('clear')
    new()
elif choice == 2:
    print ('Starting user management...')
elif choice == 3:
    print ('Rebooting the server...')
else:  # default ##
    print ('Invalid number. Try again...')
