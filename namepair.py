# A simple secret santa name pairing script
# written by plscks
# Sorry about the reccursion in main()
# I should probably not have a function calling itself.....

import os
import random
import time

a = []
b = []
c = {}


def main():
    global a
    print('Names so far: ')
    for y in a:
        print(y)
    d = input('Add name? (y/n) : ').lower()
    if d.startswith('y'):
        e = input('Full name: ')
        a.append(e)
        os.system('cls' if os.name == 'nt' else 'clear')
        main()
    else:
        mixer()


def mixer():
    global a
    truth = True
    while truth:
        truth = False
        b = list(a)
        random.shuffle(a)
        random.shuffle(b)
        c = dict(zip(a, b))
        for x in c:
            if x == c[x]:
                print('OOPS')
                truth = True
                break
    os.system('cls' if os.name == 'nt' else 'clear')
    f = input('Display who gets Scott? (y/n) : ').lower()
    if f.startswith('y'):
        print(c['Scott Himmelmann'] + ' gets Scott')
        del c['Scott Himmelmann']
        input('Press any key to confinue...')
        os.system('cls' if os.name == 'nt' else 'clear')
        input('Press any key to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in c:
            print(c[x] + ' gets ' + x)
        print('Done')
    else:
        print('Quitting.....')
        quit()

os.system('cls' if os.name == 'nt' else 'clear')
main()
