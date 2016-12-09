# A simple secret santa name pairing script

import copy
import os
import random
import time

a = []
b = []
c = {}

def main():
    global a
    d = input('Add name? (y/n) : ').lower()
    if d.startswith('y'):
        e = input('Full name: ')
        a.append(e)
        print(a)
        os.system('cls')
        main()
    else:
        mixer()

def mixer():
    global a
    b = list(a)
    random.shuffle(a)
    random.shuffle(b)
    print(a)
    print(b)
    c = dict(zip(a, b))
    print(c)
    for x in c:
        if c[x] == x:
            print(c)
            print(x)
            print('OOPS')
            mixer()
        else:
            time.sleep(0)
        print(x + ' gets ' + c[x])

os.system('cls')
main()
