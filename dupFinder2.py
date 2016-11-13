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
h = []
i = []

# d is list of files in cwd
print('Grabbing a list of files in the CWD')
# time.sleep(2)
d = os.listdir(os.getcwd())
time.sleep(1)
# print(d)
# print()
# For every file in cwd, size is obtained and added to list e
print('Creating a list of file sizes from the first list of files')
time.sleep(2)
for f in d:
    e.append(os.stat(f).st_size)
# time.sleep(1)
# print(e)
print()
# Now we will zip both lists together to form a dictionary
# print('Zipping both lists together in a dictionary')
# time.sleep(2)
# Making a dictionary that will hold the CWD file/size info
f = dict(zip(d, e))
# time.sleep(1)
# print(f)
print()
# Making a copy of the dictionary that we can edit
g = dict(zip(d, e))
# Now we will attempt to check the files for duplicate sizes
# Iterating through list of files
print('Checking for duplicate files...')
for k in f:
    # print('We are checking for duplicate file size now')
    # Saving the currently selected files size and name attributes
    tempsize = f[k]
    tempname = k
    # print('checking this file:')
    # print(tempsize)
    # print(tempname)
    # print()
    # Removing currently selected file from dictionary of files
    del g[k]
    # Checking a copy of the dictionary for same size as selected file
    for kk in g:
        if g[kk] == tempsize:
            if kk in h or kk in i:
                # print(kk + ' already dealt with')
                time.sleep(0)
            else:
                # Found a same size file, now to grab its md5 hash and checking it
                # with the selected file
                # print(kk + ' is possible duplicate of ' + tempname)
                with open(kk, 'rb') as suspectFile:
                    suspectData = suspectFile.read()
                    suspect_md5 = hashlib.md5(suspectData).hexdigest()
                with open(tempname, 'rb') as tempFile:
                    tempData = tempFile.read()
                    temp_md5 = hashlib.md5(tempData).hexdigest()
                # print(kk + ' md5 : ' + suspect_md5)
                # print(tempname + ' md5 : ' + temp_md5)
                # Checking if md5 hash is same for both files
                if suspect_md5 == temp_md5:
                    print(kk + ' is difinitively a duplicate of ' + tempname)
                    remove = input('Would you like to remove ' +
                                   kk + '? (y/n): ').lower()
                    # Match found, asking to remove
                    if remove in {'y', 'yes', 'ok', 'sure'}:
                        # print('Removing ' + kk + ' .....')
                        # print('test remove')
                        # Double checking if you'd like to remove
                        remove2 = input(
                            'Are you certain you would like to remove ' + kk + '? (y/n): ').lower()
                        if remove2 in {'y', 'yes', 'ok', 'sure'}:
                            print('Removing ' + kk)
                            print()
                            time.sleep(1)
                            # Adding kk to remove list
                            h.append(kk)
                        else:
                            print('Keeping ' + kk)
                            print()
                            time.sleep(1)
                            i.append(kk)
                    else:
                        print('Keeping ' + kk)
                        print()
                        time.sleep(1)
                        i.append(kk)
                else:
                    # print(kk + ' is the same size as ' + tempname + ' but is not the same file.')
                    time.sleep(0)
        else:
            # print(kk + ' is okay')
            time.sleep(0)
        g = dict(zip(d, e))
print()
for r in h:
    print('Removed ' + r)
    os.remove(r)
