# File listing and differentiating POF
# written by plscks
import os
import os.path
import random


c = []
d = []
e = {}
# dirname = input('\nPath to photo directory: ')
dirname = '/home/plscks/Pictures/Wallpapers/'
print('\n')
for f in os.listdir(dirname):
    if f.endswith('.jpg'):
        d.append(f)
    if f.endswith('.png'):
        d.append(f)
random.shuffle(d)
c = list(range(len(d)))
print(d)
print(c)
e = dict(zip(c, d))
print(e)
print('\n')
for s in e:
    print(e[s])
    print(e[s])
    if ((s + 1) in e) == True:
        print(e[(s + 1)])
    else:
        print(e[0])
