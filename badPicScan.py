# Program to scan for corrupt pictures in a directory
# written by plscks
# concept : https://stackoverflow.com/questions/4780424/detecting-corrupted-images-in-bash-script
#############
##  GOALS  ##
#############
# - read all file names
# - store all file names
# - verify file integrity
# - store bad file names and continue
# - allow user to delete corrupt files individually or in batch, with preview option for individual
# - exit
############
## START  ##
############
from os import listdir
from os.path import isfile, join
from PIL import Image

def readPictures():
    files = [f for f in listdir('/home/plscks/Pictures/Wallpapers') if isfile(join('/home/plscks/Pictures/Wallpapers', f))]
    keep = []
    for item in files:
        if item.endswith('.jpg'):
            keep.append(item)
        elif item.endswith('.png'):
            keep.append(item)
        elif item.endswith('.gif'):
            keep.append(item)
    return keep

if __name__ == '__main__':
    keep = readPictures()
    print keep
