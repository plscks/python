# test reading file program
# written by plscks
import fileinput
import os
import sys


os.system('cls' if os.name == 'nt' else 'clear')
print(30 * '-')
print('Open existing RO')
print(30 * '-')
ROnumber = input('RO Number: ')
ROfile = str(ROnumber) + '.txt'
