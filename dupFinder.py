# Duplicate file(wallpaper) finder and remover
# Writen by plscks

import hashlib
import os
import sys


c = []
d = []
e = {}
dirname = '/home/plscks/python/'
newfilename = '1.jpg'
for f in os.listdir(dirname):
    if f.endswith('.jpg'):
        d.append(f)
    if f.endswith('.png'):
        d.append(f)
size1 = (os.stat(newfilename)).st_size
print(str(size1))
d.remove(newfilename)
print(d)
for s in d:
    c.append((os.stat(s)).st_size)
print(c)
e = dict(zip(d, c))
print(e)
print('\n')
for t in e:
    print(e[t])
    if e[t] == size1:
        with open(newfilename, 'rb') as newCheckFile:
            newData = newCheckFile.read()
            new_md5 = hashlib.md5(newData).hexdigest()
        with open(t, 'rb') as suspectDup:
            suspectData = suspectDup.read()
            suspect_md5 = hashlib.md5(suspectData).hexdigest()
        if new_md5 == suspect_md5:
            print(str(new_md5))
            print(str(suspect_md5))
            print(str(t) + ' is a dulpicate of ' + newfilename)
            print('\n')
            print(t)
        else:
            print('Searching')
