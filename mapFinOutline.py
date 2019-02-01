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
        return doc
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

def findCoords(finalList, type):
    equations = {0 : ['x - 2','y - 2'], 1 : ['x - 1','y - 2']} etc something like this? need to figure out how to evaluate equation.
    pattern = re.compile(r'(<td height).*?(<\/td>)')
    infoNames = []
    infoTypes = []
    fileList = []
    seen = set()
    seen_add = seen.add
    for file in finalList:
        with open (file, 'rt') as in_file:
            contents = in_file.read()
            center = pull center coords
            plane = get plane
            planeNum = assign plane number
            for idx, m in enumerate(re.finditer(pattern, contents)):
                x, y = equation[idx]
                tileCoords = figure coords from center point and equation
                color1 = re.search(r'(?<=bgcolor=).*?(?=  )', m.group(0))
                tileColor = color1.group(0)
                tileDesc = get complete litel description
                tileName, tileType = tileDesc.split(',')
                if type == 'names':
                    infoNames.append('registerTileNames(' + tileCoords + ',' + planeNum + '"' + tileName + '");')
                if type == 'types':
                    infoTypes.append('registerTileNames(' + tileCoords + ',' + planeNum + '"' + tileType + '");')
                if type == 'doc':
                    fileList.append('(' + tileCoords + ' ' + plane + ')\n' + tileDesc + '\n' + color + '\n' + '\n')
    if type == 'names':
        infoNamesClean = [x for x in infoNames if not (x in seen or seen_add(x))]
        return infoNamesClean
    if type == 'types':
        infoTypesClean = [x for x in infoTypes if not (x in seen or seen_add(x))]
        return infoTypesClean
    if type == 'doc':
        fileListClean = [x for x in fileList if not (x in seen or seen_add(x))]
        return fileListClean
    
def fileOut(fileListClean):
    with open('tileInfoList.txt', 'w') as out:
        for tileInfo in fileListClean:
            out.write(tileInfo)

def scriptOut(info):
    
