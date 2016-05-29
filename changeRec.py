# Recommendation change test
# Proof of concept
# written by
# plscks
import os


def openMenu():
    global ROnumber
    global ROfile
    global ROtemp
    os.system('cls' if os.name == 'nt' else 'clear')
    print(30 * '-')
    print('Editing Recs')
    print(30 * '-')
    ROnumber = input('RO Number: ')
    ROfile = str(ROnumber) + '.txt'
    ROtemp = str(ROnumber) + '_tmp.txt'


def recChange():
    with open(ROfile, 'rt') as in_file:
        contents = in_file.read()
        in_file.close()
    print(contents)


openMenu()
os.system('cls' if os.name == 'nt' else 'clear')
recChange()
