# rhtriangle.py
# A program to find the sides of any given right triangle with two known sides
#
# Written by plscks

import math
import os

def err():
    print('\n')
    print('\n **********ERROR**********')
    print('|-------------------------|')
    print('|--Triangle not possible--|')
    print('|--Hypotenuse  mislabled--|')
    print('|--recheck your  figures--|')
    print('|-------------------------|')

os.system('clear')
a = 0
b = 0
# c = 0
d = 0
e = 0
h = 0
print('\n')
print('\nTo find the third side of any given right')
print('triangle with 2 known sides.\n')
print('------------------------------------------------')
x = input('Which side, a, b, or c {hypotenuse}?:')
if x is ('c'):
    print('\nFinding side c')
    a = int(input('\nSide a:'))
    b = int(input('\nSide b:'))
    h = math.sqrt(((a * a) + (b * b)))
    print('\nSide c is equal to:')
    print(h)
else:
    print('\nFinding side a or b')
    h = int(input('\nHypotenuse:'))
    b = int(input('\nKnown side:'))
    if b > h:
        err()
    else:
        a = math.sqrt(((h * h) - (b * b)))
        print('\nUnknown side is equal to:')
        print(a)
