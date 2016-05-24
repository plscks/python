#!/usr/bin/python
# Version 1
## Show menu ##
import os
import time
import math


# ROnumber = 0
# Lines = 0
i = 0


def new():
    global ROnumber
    global ROfile
    global f
    ROnumber = input('RO Number: ')
    ROfile = str(ROnumber) + '.txt'
    Lines = input('\nNumber of lines(13 max): ')
    Lines = int(Lines)
    with open(ROfile, 'wt') as f:
        f.write('RO number: ')
        f.write(ROnumber)
        f.write('\n')
        f.write('\n')
        for i in range(Lines):
            if 0 >= i < Lines:
                LineA = input('\nLine A: ')
                i = i + 1
                f.write('Line A: ' + str(LineA))
                recs()
            elif 1 >= i < Lines:
                LineB = input('\nLine B: ')
                i = i + 1
                f.write('\n')
                f.write('\nLine B: ' + str(LineB))
                recs()
            elif 2 >= i < Lines:
                LineC = input('\nLine C: ')
                i = i + 1
                f.write('\n')
                f.write('\nLine C: ' + str(LineC))
                recs()
            else:
                print('\nReturning to menu...')
                time.sleep(2)
                menu()


def menu():
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
        print ('Opening existing RO...')
    elif choice == 3:
        print ('Quitting!')
    else:  # default ##
        print ('Invalid number. Try again...')


def recs():
    d = {}
    recs = input('How many redomendations?: ')
    recs = int(recs)
    for j in range(recs):
        j = j + 1
        d[j] = input('Rec #' + str(j) + ': ')
        f.write('\n    Rec #' + str(j) + ': ' + d[j])


os.system('clear')
menu()
quit()
