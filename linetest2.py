# dictionary test file
# new line function proof-of-concept
# written by plscks
import itertools
import os
import string
import time


def new():
    global ro
    d = {}
    z = string.ascii_uppercase
    i = 0
    j = []
    ROnumber = input('RO Number: ')
    ROfile = str(ROnumber) + '.txt'
    Lines = input('Number of lines: ')
    Lines = int(Lines)
    with open(ROfile, 'wt') as ro:
        ro.write('RO number: ')
        ro.write(ROnumber)
        ro.write('\n')
        ro.write('\n')
        for x in range(Lines):
            i = i + 1
            letter = itertools.cycle(z)
            j.append(i)
            d = dict(zip(j, letter))
            newLine = input('Line ' + d[i] + ': ')
            ro.write('Line ' + d[i] + ': ' + newLine)
            recs()
            ro.write('\n')


def recs():
    e = {}
    recs = input('How many redomendations?: ')
    recs = int(recs)
    for k in range(recs):
        k = k + 1
        e[k] = input('Rec #' + str(k) + ': ')
        ro.write('\n    Rec #' + str(k) + ': ' + e[k])
    ro.write('\n')


new()
