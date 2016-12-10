# shuffle test written by plscks
# the aim is to take two same lists and shuffle them into a dictionary
# where no key is the same as it's value

import os
import random
import time


truth = True
while truth:
    truth = False
    a = ['a', 'b', 'c', 'd']
    b = list(a)
    random.shuffle(a)
    random.shuffle(b)
    c = dict(zip(a, b))
    for x in c:
        if x == c[x]:
            print('OOPS')
            truth = True
            break
        print(x + ' gets ' + c[x])
