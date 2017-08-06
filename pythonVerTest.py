# Is this a test?
# Just a simple proof of concept to see if I can detect
# which version of python the user is running, and act accordingly.
import sys

if (sys.version_info < (3, 0)):
    print('It has to be.')
    print('Try again using python version 3.0 or greater')
    exit()

print('The program stuff happens here???')
print('Otherwise I cant go on.')
print('No really though, the rest of the program goes here.')
