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
import urllib.request


def main:
    os.system('cls' if os.name == 'nt' else 'clear')
    user = input('USERNAME: ')
    url1 = 'https://raw.githubusercontent.com//plscks/settings/master/.bashrc'
    path1 = '/home/' + user + '/'
    file1 = url1[57:]
    if os.path.isdir(path1) == True:
        if os.path.isfile(path1 + file1 == True):
            ow1 = input(file1 + ' exists, overwrite it? (Y/N): ')
            if ow1 == 'Y':
                print('Overwriting ' + file1)
            else:
                print('Skipping ' + file1
        else:
            print('Saving ' + path1 + file1)
    else:
        print(path1 + ' Does not exist. Incorrect pathname.')
    url2 = 'https://raw.githubusercontent.com/plscks/settings/master/.emacs'
    path2 = '/home/' + user + '/'
    #url3 = 'https://raw.githubusercontent.com/plscks/settings/master/.bash_aliases'
    #path3 = 
