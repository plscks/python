#!/usr/bin/python3
# Duplicate file finder
#
# Is this a test?
# It has to be!
#
# written by plscks
import os
import time

d = []
e = []
f = {}
g = {}

# d is list of files in cwd
print('Grabbing a list of files in the CWD')
time.sleep(2)
d = os.listdir(os.getcwd())
time.sleep(1)
print(d)
print()
# For every file in cwd, size is obtained and added to list e
print('Creating a list of file sizes from the first list of files')
time.sleep(2)
for f in d:
    e.append(os.stat(f).st_size)
time.sleep(1)
print(e)
print()
# Now we will zip both lists together to form a dictionary
print('Zipping both lists together in a dictionary')
time.sleep(2)
f = dict(zip(d, e))
time.sleep(1)
print(f)
print()
g = dict(zip(d, e))
# Now we will attempt to check the files for duplicate sizes
for k in f:
    print('We are checking for duplicate file size now')
    tempsize = f[k]
    del g[k]
    if f[k] == 
    
