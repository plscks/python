# listFromFile.py written by plscks
# A quick functional test of pulling IP addresses from an existing file
# Then a test for removing items in a list
#  from a list
#
import os

#getting Current Working Directory path and setting file name
cwd = os.getcwd()
file = 'IPlist.txt'
fullFile = cwd + '/IPlist.txt'

#making a list from file and printing that list
goodIP = open(fullFile,'r').read().split('\n')
#Let's try to remove the empty component from the list
goodIP.pop()
print('------------------KNOWN GOOD IPs----------------------')
print(goodIP)
allIP = ['123.123.123.123', '124.124.124.124', '192.168.254.28', '321.321.321.321', '192.168.254.30', '457.457.457.457']
print('-----------------ALL IP ADDRESSES---------------------')
print(allIP)
badIP = [x for x in allIP if x not in goodIP]
print('----------ALL IPs WITH KNOWN GOOD REMOVED-------------')
print(badIP)
