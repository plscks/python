# Recommendation change test
# Proof of concept
# written by
# plscks
import os
import time


def openMenu():
    global ROnumber
    global ROfile
    global ROtemp
    os.system('cls' if os.name == 'nt' else 'clear')
    print(30 * '-')
    print('Editing Recs')
    print(30 * '-')
    ROnumber = input('RO Number: ')
    ROfile = str(ROnumber) + '.txt'
    ROtemp = str(ROnumber) + '_tmp.txt'


def recChange():
    global in_file
    lines = []
    with open(ROfile, 'rt') as in_file:
        for line in in_file:
            lines.append(line)
    for element in lines:
        print(element, end='')
    print('\n')
    for linenum, line in enumerate(lines):
        print(linenum, line, end='')


openMenu()
os.system('cls' if os.name == 'nt' else 'clear')
recChange()
in_file.close()
