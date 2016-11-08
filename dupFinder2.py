#!/usr/bin/python3
# Duplicate file finder
#
# Is this a test?
# It has to be!
#
# written by plscks
import os

d = []
e = []

# d is list of files in cwd
d = os.listdir(os.getcwd())
# For every file in cwd, size is obtained and added to list e
for f in d:
    e.append(os.stat(f).st_size)
print(d)
print()
print(e)
# Now we will zip both lists together to form a dictionary
