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
from PIL import Image
