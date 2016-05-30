# test reading file program
# written by plscks
# import fileinput
import os
# import sys


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
            openMenu()
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


openMenu()
mainMenu()
print('changed some stuff maybe?')
quit()  # should go back to main menu
