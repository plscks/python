#!/usr/bin/python3
# Current Working Directory test.
# written by plscks
import os

print('This is a test of finding the current working directory (CWD)')
print('')
print('We will test by using __File__ ')
print('Here we go!')
print('')
# print(__file__)
# print(os.chdir(os.path.dirname(__file__)))
print(os.getcwd())
print('Turns out "print(os.getcwd())" only works if you execute the script with a shebang')
print('Hmm...')
print('Nevermind, works just fine both ways then???')
print('Whatever, onwards!')
