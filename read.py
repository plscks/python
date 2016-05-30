# test reading file program
# written by plscks
# import fileinput
import os
# import sys


def newLineExit():
    c = input('Change recommendation? (y/n): ')
    if c == 'y':
        recChange()
    elif c == 'n':
        quit()  # placeholder for main menu.py
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
            quit()  # placeholder should go to main menu.py
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
    print('Changed a rec?')
    in_file.close()
    out_file.close()


openMenu()
mainMenu()
print('changed some stuff maybe?')
quit()  # should go back to main menu
