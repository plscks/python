#!/usr/bin/python3
# Duplicate file finder
#
# Is this a test?
# It has to be!
#
# written by plscks
import os
import time
import hashlib

d = []
e = []
f = {}
g = {}

# d is list of files in cwd
print('Grabbing a list of files in the CWD')
#time.sleep(2)
d = os.listdir(os.getcwd())
#time.sleep(1)
print(d)
print()
# For every file in cwd, size is obtained and added to list e
print('Creating a list of file sizes from the first list of files')
#time.sleep(2)
for f in d:
    e.append(os.stat(f).st_size)
#time.sleep(1)
print(e)
print()
# Now we will zip both lists together to form a dictionary
print('Zipping both lists together in a dictionary')
#time.sleep(2)
# Making a dictionary that will hold the CWD file/size info
f = dict(zip(d, e))
#time.sleep(1)
print(f)
print()
# Making a copy of the dictionary that we can edit
g = dict(zip(d, e))
# Now we will attempt to check the files for duplicate sizes
# Iterating through list of files
for k in f:
    print('We are checking for duplicate file size now')
    # Saving the currently selected files size and name attributes
    tempsize = f[k]
    tempname = k
    print('checking this file:')
    print(tempsize)
    print(tempname)
    print()
    # Removing currently selected file from dictionary of files
    del g[k]
    # Checking a copy of the dictionary for same size as selected file
    for kk in g:
        if g[kk] == tempsize:
            # Found a same size file, now to grab its md5 hash and checking it with the selected file
            print(kk + ' is possible duplicate of ' + tempname)
            with open(kk, 'rb') as suspectFile:
                suspectData = suspectFile.read()
                suspect_md5 = hashlib.md5(suspectData).hexdigest()
            with open(tempname, 'rb') as tempFile:
                tempData = tempFile.read()
                temp_md5 = hashlib.md5(tempData).hexdigest()
            print(kk + ' md5 : ' + suspect_md5)
            print(tempname + ' md5 : ' + temp_md5)
            if suspect_md5 == temp_md5:
                print(kk + ' is difinitively a duplicate of ' + tempname)
                remove = input('Would you like to remove ' + kk + '? (y/n): ')
                if remove == 
            else:
                print(kk + ' is the same size as ' + tempname + ' but is not the same file.')
        else:
            print(kk + ' is okay')
        g = dict(zip(d, e))
