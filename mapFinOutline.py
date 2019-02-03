# Outline for final Nexus Clash mapping program
# Used to change and modify the Nexus Clash HYPERMAP script
# This is clearly a project for fun. 
# written by plscks
#
# ##############################
# ## Stuff I'd like it to do: ##
# ##############################
#
# [X] - Have command line args for output to file or modify script.js or output to file as array
# [X] - Search current directory for html files
# [X] - Check that they are html data if not, record offending file
# [X] - Locate coordinate & plane of center tile in one file
# [X] - find map data, pull tile color and description and figure coordinates based on center coordinate
# [X] - load coordinate, description, and color from each file into a master list
# [X] - Once done with all files, check master list for duplicates and remove.
# [X] - Output master list as a seperate file
# [] - If specified, output data directly into script.js
# [-] - If specified output data as array list
# [] - have completed message indicating how many files


def argParse(argv):
    if no argument:
        return doc
    if script argument:
        return script
    if array argument:
        return array

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
    arrayList = []
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
                tileDesc = get complete tile description
                tileName, tileType = tileDesc.split(',')
                if type == 'names':
                    infoNames.append('registerTileNames(' + tileCoords + ',' + planeNum + '"' + tileName + '");')
                if type == 'types':
                    infoTypes.append('registerTileNames(' + tileCoords + ',' + planeNum + '"' + tileType + '");')
                if type == 'doc':
                    fileList.append('(' + tileCoords + ' ' + plane + ')\n' + tileDesc + '\n' + tileColor + '\n' + '\n')
                if type == 'array':
                    arrayList.append(tilecoords + '' + plane + '' + tileDesc + '' + tileColor)
    if type == 'names':
        infoNamesClean = [x for x in infoNames if not (x in seen or seen_add(x))]
        return infoNamesClean
    if type == 'types':
        infoTypesClean = [x for x in infoTypes if not (x in seen or seen_add(x))]
        return infoTypesClean
    if type == 'doc':
        fileListClean = [x for x in fileList if not (x in seen or seen_add(x))]
        return fileListClean
    if type == 'array':
        arrayListClean = [x for x in arrayList if not (x in seen or seen_add(x))]
        return arrayListClean
    
def fileOut(fileListClean):
    with open('tileInfoList.txt', 'w') as out:
        for tileInfo in fileListClean:
            out.write(tileInfo)

def scriptOut(info):
    stuff

def arrayOut(arrayListClean):
    # process array list
    # [] - find highest y value
    # [] - create 2 lists that many values long
    # [] - fill lists with placeholders
    # [] - create list of all same value x coordinates
    # [] - insert info and color of 1st x coordinate values into list in proper numerical place.
    ex
    '1, 2 tile color', '1, 3 tile color', '1, 4 tile color', '1, 5 tile color'
    '2, 1 tile color', '2, 2 tile color', '2, 3 tile color', '2, 4 tile color', '2, 5 tile color'
    '3, 1 tile color', '3, 3 tile color', '3, 4 tile color', '3, 5 tile color'
    '4, 2 tile color', '4, 3 tile color', '4, 4 tile color', '4, 5 tile color'
    '5, 1 tile color', '5, 2 tile color', '5, 3 tile color', '5, 4 tile color'

    highest y = 5

    color = [0, 0, 0, 0, 0]
    desc = [0, 0, 0, 0, 0]

    # after arranging by y value in numerical order
    x = ['1, 2 tile color', '1, 3 tile color', '1, 4 tile color', '1, 5 tile color']
    
    # add x into color in proper place in list numerically using zero as placeholder for no value
    color = [0, '1, 2 tile color', '1, 3 tile color', '1, 4 tile color', '1, 5 tile color']
    array.append(color)

    # then next x coord row
    x = ['2, 1 tile color', '2, 2 tile color', '2, 3 tile color', '2, 4 tile color', '2, 5 tile color']
    array.append(color)

    # then next
    x = ['3, 1 tile color', 0, '3, 3 tile color', '3, 4 tile color', '3, 5 tile color']
    array.append(color)

    # ..... so on?
