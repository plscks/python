# File listing and differentiating POF
# written by plscks
import os
import os.path


d = []
# dirname = input('\nPath to photo directory: ')
dirname = '/home/plscks/Pictures/Wallpapers/'
print('\n')
for f in os.listdir(dirname):
    if f.endswith('.jpg'):
        d.append(f)
    if f.endswith('.png'):
        d.append(f)
for s in d:
