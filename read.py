# test reading file program
# written by plscks
# import fileinput
import os
# import sys


os.system('cls' if os.name == 'nt' else 'clear')
print(30 * '-')
print('Open existing RO')
print(30 * '-')
ROnumber = input('RO Number: ')
ROfile = str(ROnumber) + '.txt'
ROtemp = str(ROnumber) + '_tmp.txt'
f1 = open(ROfile, 'r')
f2 = open(ROtemp, 'w')
for line in f1:
    f2.write(line.replace('Line A:', '*Line A:'))
f1.close()
f2.close()
os.remove(ROtemp)
os.rename(ROtemp, ROfile)
print('edited file?')