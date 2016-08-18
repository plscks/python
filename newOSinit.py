# A script to setup fresh linux installs with my personal
# bash and emacs preferences
# written by plscks
#
# ROUGH OUTLINE
#
# 1. pull files off GitHub and store in working dir
# 2. check if files exist in users home dir
# 3. prompt user if they want to overright existing files.
# 4. move files to thier paths
# 5. remove temporary files in working dir
import os
import shutil
import time
import urllib.request


os.system('cls' if os.name == 'nt' else 'clear')
user = input('USERNAME: ')
url1 = 'https://raw.githubusercontent.com//plscks/settings/master/.bashrc'
path1 = '/home/' + user + '/'
file1 = url1[57:]
url2 = 'https://raw.githubusercontent.com/plscks/settings/master/.emacs'
path2 = '/home/' + user + '/'
file2 = url2[57:]
# url3 = 'https://raw.githubusercontent.com/plscks/settings/master/.bash_aliases'
# path3 =
mainIn1()


def mainIn1():
    if os.path.isdir(path1) == True:
        if os.path.isfile(path1 + file1 == True):
            ow1 = input(file1 + ' exists, overwrite it? (Y/N): ')
            if ow1 == 'Y':
                print('Overwriting ' + file1)
                write1()
            else:
                print('Skipping ' + file1)
                mainIn2()
        else:
            print('Saving ' + path1 + file1)
            write1()
    else:
        print(path1 + ' Does not exist. Incorrect pathname.')
        global path1 = input('Input correct path: ')
        write1()


def write1():
    with urllib.request.urlopen(url1) as responce1, open(path1 + file1, 'wb') as temp1:
        shutil.copyfileobj(responce1, temp1)
    time.sleep(2)
    mainIn2()


def mainIn2():
    if os.path.isdir(path2) == True:
        if os.path.isfile(path2 + file2 == True):
            ow2 = input(file2 + ' exists, overwrite it? (Y/N): ')
            if ow2 == 'Y':
                print('Overwriting ' + file2)
                write2()
            else:
                print('Skipping ' + file2)
                print('')
                print('Skipping both files. Exiting program')
        else:
            print('Saving ' + path2 + file2)
            write2()
    else:
        print(path2 + ' Does not exist. Incorrect pathname.')
        global path2 = input('Input correct path: ')
        write2()


def write2():
    with urllib.request.urlopen(url2) as responce2, open(path2 + file2, 'wb') as temp2:
        shutil.copyfileobj(responce2, temp2)
    time.sleep(2)
    print('Files copied. Enjoy your settings. Peace.')
    quit()
