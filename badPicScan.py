# Program to scan for corrupt pictures in a directory
# written by plscks
# concept : https://stackoverflow.com/questions/4780424/detecting-corrupted-images-in-bash-script
#############
##  GOALS  ##
#############
# - [X] - read all picture file names
# - [X] - store all picture file names
# - [X] - verify file integrity
# - [X] - store bad file names and continue
# - []  - allow user to delete corrupt files individually or in batch, with preview option for individual
# - []  - exit
############
## START  ##
############
import os
from os import listdir
from os.path import isfile, join
from PIL import Image

def readPictures(cwd):
    """Read all .jpg .png .gif in current working directory returns them as a list"""
    
    files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
    keep = []
    for item in files:
        if item.endswith('.jpg'):
            keep.append(item)
        elif item.endswith('.png'):
            keep.append(item)
        elif item.endswith('.gif'):
            keep.append(item)
    return keep

def verifyPictures(list, cwd):
    """Verifies integrity of pictures in cwd as input from filename list, returns list of corrupt pictures"""
    
    rv = []
    for f in list:
        try:
            test = Image.open(cwd + '/' + f)
            test.verify()
        except:
            rv.append(f)
    return rv

def removePictures(list, cwd):
    """Allow user to choose files from input list to delete in CWD"""

    

if __name__ == '__main__':
    cwd = os.getcwd()
    keep = readPictures(cwd)
    bad = verifyPictures(keep, cwd)
    print(bad)
