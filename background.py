#!/usr/bin/python3
# UbunutMate Wallpaper slideshow maker
# written by plscks
import datetime
import os
import os.path
import random


now = now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
c = []
d = []
e = {}
dirname = '/home/plscks/Pictures/Wallpapers/'
for f in os.listdir(dirname):
    if f.endswith('.jpg'):
        d.append(f)
    if f.endswith('.png'):
        d.append(f)
random.shuffle(d)
c = list(range(len(d)))
e = dict(zip(c, d))
f = str(c[-1] +1)

with open((dirname + 'background-1.xml'), 'wt+') as back:
    back.write('<background>')
    back.write('\n  <starttime>')
    back.write('\n    <year>2009</year>')
    back.write('\n    <month>08</month>')
    back.write('\n    <day>04</day>')
    back.write('\n    <hour>00</hour>')
    back.write('\n    <minute>00</minute>')
    back.write('\n    <second>00</second>')
    back.write('\n    </starttime>')
    back.write('\n<!-- This animation will start at midnight. -->')
    for s in e:
        back.write('\n  <static>')
        back.write('\n    <duration>600.0</duration>')
        back.write('\n    <file>' + dirname + e[s] + '</file>')
        back.write('\n  </static>')
        back.write('\n  <transition>')
        back.write('\n    <duration>5.0</duration>')
        back.write('\n    <from>' + dirname + e[s] + '</from>')
        if ((s + 1) in e) == True:
            back.write('\n    <to>' + dirname + e[(s + 1)] + '</to>')
            back.write('\n  </transition>')
        else:
            back.write('\n    <to>' + dirname + e[0] + '</to>')
            back.write('\n  </transition>')
    back.write('\n</background>')
print(now + '    ' + 'Randomized and created slideshow of ' + f + ' different wallpapers')
