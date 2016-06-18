# Menu.py for tracking Repair orders
# Written by plscks

import itertools
import os
import string
import time


# ROnumber = 0
# Lines = 0
i = 0
ro = 'f'


def new():
    global ROnumber
    global ROfile
    global ro
    d = {}
    z = string.ascii_uppercase
    i = 0
    j = []
    print(30 * '-')
    print('New RO')
    print(30 * '-')
    ROnumber = input('RO Number: ')
    ROfile = str(ROnumber) + '.txt'
    Lines = input('\nNumber of lines: ')
    Lines = int(Lines)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(30 * '-')
    print('RO Number: ' + ROnumber)
    print(30 * '-')
    with open(ROfile, 'wt') as ro:
        ro.write('RO number: ')
        ro.write(ROnumber)
        ro.write('\n')
        ro.write('\n')
        for i in range(Lines):
            i = i + 1
            letter = itertools.cycle(z)
            j.append(i)
            d = dict(zip(j, letter))
            print('\n')
            newLine = input('Line ' + d[i] + ': ')
            ro.write('Line ' + d[i] + ': ' + newLine)
            recs()
            ro.write('\n')
            ro.write('\n')
        else:
            print('\nReturning to menu...')
            time.sleep(2)
            menu()
    ro.close()


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(30 * '-')
    print('   M A I N - M E N U')
    print(30 * '-')
    print('1. New RO')
    print('2. Existing RO')
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
        os.system('cls' if os.name == 'nt' else 'clear')
        new()
    elif choice == 2:
        print('Opening RO...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        openMenu()
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
        ro.write('\n    Rec #' + str(j) + ': ' + d[j])


def newLineExit():
    c = input('Change recommendation? (y/n): ')
    if c == 'y':
        recChange()
    elif c == 'n':
        menu()
    else:
        print('Invalid entry! Try again please :P')
        newLineExit()


def newLine():
    line = input('Line: ')
    if line == '':
        print('Invalid entry! Try again please.')
        newLine()
    else:
        ROline = 'Line ' + str(line)
        ROdesc = input('New line: ')
        ROnew = '*' + str(ROline) + ': ' + str(ROdesc) + '\n'
        f1 = open(ROfile, 'r')
        f2 = open(ROtemp, 'w')
        for line in f1:
            f2.write(ROnew if ROline in line else line)
        f1.close()
        f2.close()
        os.remove(ROfile)
        os.rename(ROtemp, ROfile)
        newLineExit()


def openMenu():
    global ROnumber
    global ROfile
    global ROtemp
    os.system('cls' if os.name == 'nt' else 'clear')
    print(30 * '-')
    print('Open existing RO')
    print(30 * '-')
    ROnumber = input('RO Number: ')
    ROfile = str(ROnumber) + '.txt'
    ROtemp = str(ROnumber) + '_tmp.txt'
    os.system('cls' if os.name == 'nt' else 'clear')
    print(30 * '-')
    print('ORIGINAL RO')
    print(30 * '-')
    with open(ROfile, 'rt') as orig:
        origContent = orig.read()
        print(origContent)
    orig.close()
    mainMenu()


def mainMenu():
    a = input('Change a line? (y/n): ')
    if a == 'y':
        newLine()
    elif a == 'n':
        b = input('Change a recommendation? (y/n): ')
        if b == 'y':
            recChange()
        elif b == 'n':
            print('Returning to menu')
            menu()
        else:
            print('Invalid entry! Try again please.')
            mainMenu()
    else:
        print('Invalid entry! Try again please.')
        mainMenu()


def recChange():
    substrLine = input('Which line\'s recommendation to change?: ')
    substrLine = 'Line ' + substrLine
    recNum = input('Which rec #?: ')
    recDesc = input('New recommendation: ')
    lines = []
    with open(ROfile, 'rt') as in_file:
        for line in in_file:
            lines.append(line)
    for lineNum, line in enumerate(lines):
        index = 0
        st = lines[lineNum]
        while index < len(st):
            index = st.find(substrLine, index)
            if index == -1:
                break
            lineNumB = lineNum
            index += len(substrLine)
    recNumB = int(lineNumB) + int(recNum)
    lines[recNumB] = '   *Rec #' + str(recNum) + ': ' + recDesc + '\n'
    with open(ROfile, 'w') as out_file:
        out_file.writelines(lines)
    in_file.close()
    out_file.close()
    d = input('Change another recommendation? (y/n):')
    if d == 'y':
        recChange()
    elif d == 'n':
        menu()
    else:
        print('Invalid entry! Try again please!')
        ERR(mainMenu())


def ERR(funct):
    print('Invalid entry! Try again please')
    time.sleep(2)
    funct


os.system('cls' if os.name == 'nt' else 'clear')
menu()
os.system('cls' if os.name == 'nt' else 'clear')
quit()
