#!/usr/bin/python3
# Duplicate file finder
#
# Is this a test?
# It has to be!
#
# written by plscks
# p.s. - sorry o_0

import os
import time
import hashlib

d = []
e = []
f = {}
g = {}
h = []
i = []

print('Grabbing a list of files in the CWD')
d = os.listdir(os.getcwd())
time.sleep(1)
print('Creating a list of file sizes from the first list of files')
time.sleep(2)
for f in d:
    e.append(os.stat(f).st_size)
print()
f = dict(zip(d, e))
print()
g = dict(zip(d, e))
print('Checking for duplicate files...')
for k in f:
    tempsize = f[k]
    tempname = k
    del g[k]
    for kk in g:
        if g[kk] == tempsize:
            if kk in h or kk in i:
                time.sleep(0)
            else:
                with open(kk, 'rb') as suspectFile:
                    suspectData = suspectFile.read()
                    suspect_md5 = hashlib.md5(suspectData).hexdigest()
                with open(tempname, 'rb') as tempFile:
                    tempData = tempFile.read()
                    temp_md5 = hashlib.md5(tempData).hexdigest()
                if suspect_md5 == temp_md5:
                    print(kk + ' is difinitively a duplicate of ' + tempname)
                    # Need to check age of files here and ask if user wants to remove the older file.
                    remove = input('Would you like to remove ' + kk + '? (y/n): ').lower()
                    if remove in {'y', 'yes', 'ok', 'sure'}:
                        remove2 = input('Are you certain you would like to remove ' + kk + '? (y/n): ').lower()
                        if remove2 in {'y', 'yes', 'ok', 'sure'}:
                            print('Removing ' + kk)
                            print()
                            time.sleep(1)
                            h.append(kk)
                            i.append(kk)
                            i.append(tempname)
                        else:
                            print('Keeping ' + kk)
                            print()
                            time.sleep(1)
                            i.append(kk)
                            i.append(tempname)
                    else:
                        print('Keeping ' + kk)
                        print()
                        time.sleep(1)
                        i.append(kk)
                        i.append(tempname)
                else:
                    time.sleep(0)
        else:
            time.sleep(0)
        g = dict(zip(d, e))
print()
for r in h:
    print('Removed ' + r)
    os.remove(r)
