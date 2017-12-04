#!/usr/bin/python3
# Polybar mocp info display program
# written by plscks
# here is a bold attempt to display info about what's currently playing in mocp
# without causing repeated core dumps
# HERE GOES NOTHING!!!
#
# there are way to many 'quit()'s in here, oh well.....
#
# BLAGHRTHGGRRR! the core dumps I was getting were caused by moc V2.5.2
# updating to mocp V2.6-alpha3 solves the repeated core dumps

import re
import subprocess

#info = subprocess.getoutput('mocp --info')
output = subprocess.run(['mocp', '--info'], stdout=subprocess.PIPE)
info = output.stdout.decode("utf-8")

S = re.search('State: (.+?)\\n', info)
if S:
    state = S.group(1)
f = re.search('File: (.+?)\\n', info)
if f:
    file = f.group(1)
A = re.search('Artist: (.+?)\\n', info)
if A:
    artist = A.group(1)
a = re.search('Album: (.+?)\\n', info)
if a:
    album = a.group(1)
s = re.search('SongTitle: (.+?)\\n', info)
if s:
    song = s.group(1)


if state == 'PAUSE':
    print('Paused.....')
else:
    if file == 'http://192.168.254.31:8001/mpd.mp3':
        print(song)
    else:
        print(artist + ' - ' + album + ' - ' + song)
