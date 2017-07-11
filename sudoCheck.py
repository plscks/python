# sudo check by plscks
# This doesn't work very well at all
# oh poo

import os

if os.geteuid() != 0:
    exit("***Elevated permissions are required\n***Try again with sudo or as root.....")

print('Root aquired, it\'s fun time!')
