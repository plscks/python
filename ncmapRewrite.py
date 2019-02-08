# Mapping program for Nexus Clash
#
# Ideally this should be able to take raw page source and pull map info out of it.
# The info that gets pulled out should be able to be dumped to human readable text file
# Google Sheets importable array in a text file, to use a spreadsheet as a map
# And able to be directly imported into the HYPERMAP script.js for production use
#
# This is very much a work in progress
# Written by plscks in python 3.7
#
##############################
## Stuff I'd like it to do: ##
##############################
#
# [X] - Have command line args for output to file or modify script.js or output to file as array
# [X] - Search current directory for html files
# [X] - Check that they are corect html data if not, record offending file
# [] - Locate coordinate of center tile in one file
# [X] - Be able find and  handle more than 3 planes
# [] - find map data; pull tile color and description and figure coordinates based on center coordinate
# [] - load coordinate, description, and color from each file into a master list
# [] - Once done with all files, check master list for duplicates and remove.
# [] - Output master list as a seperate file
# [] - If specified, output data directly into script.js
# [] - If specified output data as array list
# [] - have completed message indicating how many files
#
###########
## USAGE ##
###########
# python ncmapRewrite.py [OPTION] [PLANE]
#
#    [PLANE]   Select plane to output data for no option will select all planes
#    -f        Output to tileInfoList.txt (DEFAULT)
#    -s        Direct ouput to script.js(must be in local dir)
#    -a        Output as array of correctly organized values for importing to sheets spread sheet
#
import argparse
from collections import OrderedDict
import os
from os import listdir
from os.path import isfile, join
import re

def parse():
    """Parse the command line input into something useful"""
    
    parser = argparse.ArgumentParser(description="Pull map information from Nexus Clash html source files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--array", action="store_true", help='Output as array of values for importing to sheets spread sheet')
    group.add_argument("-f", "--file", action="store_true", help='Output to tileInfoList.txt')
    group.add_argument("-s", "--script", action="store_true", help='Direct ouput to script.js(must be in local dir)')
    parser.add_argument("plane", nargs='?', default='all', help="Enter specific plane data is needed for, no entry will assume all planes")
    args = parser.parse_args()
    if args.array == True:
        kind = 'array'
        out = kind, args.plane.lower()
        return out
    elif args.file == True:
        kind = 'file'
        out = kind, args.plane.lower()
        return out
    elif args.script == True:
        kind = 'script'
        out = kind, args.plane.lower()
        return out

def readFiles(cwd):
    """Read files in current directory, create a list of all .html files, and then verify they are the proper files"""

    files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
    allFiles = []
    keep = []
    for item in files:
        if item.endswith('.html'):
            allFiles.append(item)
    for htmlFile in allFiles:
        with open (htmlFile, 'rt') as in_file:
            try:
                contents = in_file.read()
                isCorrect1 = re.search(r'\d{1,2}\, \d{1,2}(?= \w)', contents)
                isCorrect = isCorrect1.group(0)
                keep.append(htmlFile)
            except UnicodeDecodeError:
                pass
            except AttributeError:
                pass
    return keep

def mainData(rawData, reqPlane, reqKind):
    """Main file operations start here and are deligated out to different functions"""
    
    for html in rawData:
        with open (html, 'rt') as in_file:
            contents = in_file.read()
            try:
                planeInfo = collectPlane(reqPlane, contents)
                planeName =  list(planeInfo.values())[0]
                planeNum = list(planeInfo.keys())[0]
                # print('PLANE NAME: ' + planeName + '\n' + 'PLANE NUMBER: ' + str(planeNum))
            except AttributeError:
                pass

def collectCenter(contents):
    """Collects the center coordinate of the file that is opened"""
    
    pass
    
def collectPlane(reqPlane, contents):
    """Collects the plane information and adds planes if they are in the data but not known"""
    
    planeInfo = {}
    newPlane = OrderedDict()
    newPlane['laurentia'] = 0
    newPlane['elysium'] = 1
    newPlane['stygia'] = 2
    try:
        planeRaw = re.search(r'(?<=\d ).*(?=, a <a)', contents)
        plane = planeRaw.group(0)
        pass
    except AttributeError:
        planeRaw = re.search(r'(?<=\d ).*(?=, an <a)', contents)
        plane = planeRaw.group(0)
        pass
    if reqPlane == plane.lower() or reqPlane == 'all':
        if plane.lower() in newPlane:
            planeNum = newPlane[plane.lower()]
        else:
            allPlanes = list(newPlane.items())
            junk, new = allPlanes[-1]
            new = new + 1
            newPlane[plane.lower()] = new
            planeNum = newPlane[plane.lower()]
        planeInfo[planeNum] = plane
        return planeInfo
    else:
        pass
                
if __name__ == "__main__":
    kind, plane = parse()
    cwd = os.getcwd()
    htmlFileList = readFiles(cwd)
    print(htmlFileList)
    mainData(htmlFileList, plane, kind)
