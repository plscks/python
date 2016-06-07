# linetesttest.py for testing my new line function also
# Written by plscks

import os
import time


def new():
    global ROnumber
    global ROfile
    global ro
    print(30 * '-')
    print('New RO')
    print(30 * '-')
    ROnumber = input('RO Number: ')
    ROfile = str(ROnumber) + '.txt'
    Lines = input('\nNumber of lines(13 max): ')
    Lines = int(Lines)
    with open(ROfile, 'wt') as ro:
        ro.write('RO number: ')
        ro.write(ROnumber)
        ro.write('\n')
        ro.write('\n')
        for i in range(Lines):
