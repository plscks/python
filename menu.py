# Menu.py for tracking Repair orders
# Written by plscks
import os
import time


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
            if i == 0:
                LineA = input('\nLine A: ')
                f.write('Line A: ' + str(LineA))
                recs()
            elif i == 1:
                LineB = input('\nLine B: ')
                f.write('\n')
                f.write('\nLine B: ' + str(LineB))
                recs()
            elif i == 2:
                LineC = input('\nLine C: ')
                f.write('\n')
                f.write('\nLine C: ' + str(LineC))
                recs()
            elif i == 3:
                LineD = input('\nLine D: ')
                f.write('\n')
                f.write('\nLine D: ' + str(LineD))
                recs()
            elif i == 4:
                LineE = input('\nLine E: ')
                f.write('\n')
                f.write('\nLine E: ' + str(LineE))
                recs()
            elif i == 5:
                LineF = input('\nLine F: ')
                f.write('\n')
                f.write('\nLine F: ' + str(LineF))
                recs()
            elif i == 6:
                LineG = input('\nLine G: ')
                f.write('\n')
                f.write('\nLine G: ' + str(LineG))
                recs()
            elif i == 7:
                LineH = input('\nLine H: ')
                f.write('\n')
                f.write('\nLine H: ' + str(LineH))
                recs()
            elif i == 8:
                LineI = input('\nLine I: ')
                f.write('\n')
                f.write('\nLine I: ' + str(LineI))
                recs()
            elif i == 9:
                LineJ = input('\nLine J: ')
                f.write('\n')
                f.write('\nLine J: ' + str(LineJ))
                recs()
            elif i == 10:
                LineK = input('\nLine K: ')
                f.write('\n')
                f.write('\nLine K: ' + str(LineK))
                recs()
            elif i == 11:
                LineL = input('\nLine L: ')
                f.write('\n')
                f.write('\nLine L: ' + str(LineL))
                recs()
            elif i == 12:
                LineM = input('\nLine M: ')
                f.write('\n')
                f.write('\nLine M: ' + str(LineM))
                recs()
        else:
            print('\nReturning to menu...')
            time.sleep(2)
            menu()


def menu():
    os.system('clear')
    print(30 * '-')
    print('   M A I N - M E N U')
    print(30 * '-')
    print('1. New RO')
    print('2. Existing RO - NOT WORKING YET')
    print('3. Quit')
    print(30 * '-')
    # Get input ###
    choice = input('Enter your choice [1-3] : ')
    # Convert string to int type ##
    choice = int(choice)
    # Take action as per selected menu-option ###
    if choice == 1:
        print('Opening new RO...')
        time.sleep(2)
        os.system('clear')
        new()
    elif choice == 2:
        print('Work in progress...')
        time.sleep(2)
        os.system('clear')
        open()
    elif choice == 3:
        print('Quitting!')
    else:  # default ##
        print('Invalid number. Try again...')
        time.sleep(2)
        menu()


def recs():
    d = {}
    recs = input('How many redomendations?: ')
    recs = int(recs)
    for j in range(recs):
        j = j + 1
        d[j] = input('Rec #' + str(j) + ': ')
        f.write('\n    Rec #' + str(j) + ': ' + d[j])


def open():



os.system('clear')
menu()
os.system('clear')
quit()
