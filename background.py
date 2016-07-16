# UbunutMate Wallpaper slideshow maker
# written by plscks
import os
import os.path


d = []
dirname = '/home/plscks/Pictures/Wallpapers/'
for f in os.listdir(dirname):
    if f.endswith('.jpg'):
        d.append(f)
    if f.endswith('.png'):
        d.append(f)


with open('background-1.xml', 'wt') as back:
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
    for s in d:
        back.write('\n  <static>')
        back.write('\n    <duration>600.0</duration>')
        back.write('\n    <file>' + dirname + s + '</file>')
        back.write('\n  </static>')
    back.write('\n</background>')
