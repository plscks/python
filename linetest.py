# linetest.py for testing my new line function
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
            if i == 0:
                LineA = input('\nLine A: ')
                ro.write('Line A: ' + str(LineA))
                recs()
            elif i == 1:
                LineB = input('\nLine B: ')
                ro.write('\n')
                ro.write('\nLine B: ' + str(LineB))
                recs()
            elif i == 2:
                LineC = input('\nLine C: ')
                ro.write('\n')
                ro.write('\nLine C: ' + str(LineC))
                recs()
            elif i == 3:
                LineD = input('\nLine D: ')
                ro.write('\n')
                ro.write('\nLine D: ' + str(LineD))
                recs()
            elif i == 4:
                LineE = input('\nLine E: ')
                ro.write('\n')
                ro.write('\nLine E: ' + str(LineE))
                recs()
            elif i == 5:
                LineF = input('\nLine F: ')
                ro.write('\n')
                ro.write('\nLine F: ' + str(LineF))
                recs()
            elif i == 6:
                LineG = input('\nLine G: ')
                ro.write('\n')

                ro.write('\nLine G: ' + str(LineG))
                recs()
            elif i == 7:
                LineH = input('\nLine H: ')
                ro.write('\n')
                ro.write('\nLine H: ' + str(LineH))
                recs()
            elif i == 8:
                LineI = input('\nLine I: ')
                ro.write('\n')
                ro.write('\nLine I: ' + str(LineI))
                recs()
            elif i == 9:
                LineJ = input('\nLine J: ')
                ro.write('\n')
                ro.write('\nLine J: ' + str(LineJ))
                recs()
            elif i == 10:
                LineK = input('\nLine K: ')
                ro.write('\n')
                ro.write('\nLine K: ' + str(LineK))
                recs()
            elif i == 11:
                LineL = input('\nLine L: ')
                ro.write('\n')
                ro.write('\nLine L: ' + str(LineL))
                recs()
            elif i == 12:
                LineM = input('\nLine M: ')
                ro.write('\n')
                ro.write('\nLine M: ' + str(LineM))
                recs()
        else:
            print('\nquitting...')
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
    ro.close()


def recs():
    d = {}
    recs = input('How many redomendations?: ')
    recs = int(recs)
    for j in range(recs):
        j = j + 1
        d[j] = input('Rec #' + str(j) + ': ')
        ro.write('\n    Rec #' + str(j) + ': ' + d[j])


new()
