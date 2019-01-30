# Outline for final Nexus Clash mapping program
# Used to change and modify the Nexus Clash HYPERMAP script
# This is clearly a project for fun. 
# written by plscks
#
# ##############################
# ## Stuff I'd like it to do: ##
# ##############################
#
# [] - Have command line args for output to file or modify script.js
# [] - Search current directory for html files
# [] - Check that they are html data if not, record offending file
# [] - Locate coordinate & plane of center tile in one file
# [] - find map data, pull tile color and description and figure coordinates based on center coordinate
# [] - load coordinate, description, and color from each file into a master list
# [] - Once done with all files, check master list for duplicates and remove.
# [] - Output master list as a seperate file
# [] - If specified, output data directly into script.js
# [] - have completed message indicating how many files


def argParse(argv):
    if no argument:
        return file
    if script.js argument:
        return script

def readFiles(cwd):
    find html files
    return listOfFilesToKeep

def checkfiles(listOfFileToKeep):
    if '<!-- saved from url=' is there:
        remove from list
    else:
        return finalList

def findCoords(finalList):
    equations = {0 : ['x - 2','y - 2'], 1 : ['x - 1','y - 2']} etc
    pattern = re.compile(r'(<td height).*?(<\/td>)')
    with open (inputfile, 'rt') as in_file:
        
    for idx, m in enumerate(re.finditer(pattern, contents)):
        x, y = equation[idx]
        
