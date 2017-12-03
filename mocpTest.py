#!/usr/bin/python3
# Polybar mocp info display program
# written by plscks
# here is a bold attempt to display info about what's currently playing in mocp
# without causing repeated core dumps
# HERE GOES NOTHING!!!
#
# there are way to many 'quit()'s in here, oh well.....

import re
import subprocess

info = subprocess.getoutput('mocp --info')
if info == '\nFATAL_ERROR: The server is not running!\n':
    print('mocp is not running!')
    quit()
else:
    S = re.search('State: (.+?)\n', info)
    if S:
        state = S.group(1)
    f = re.search('File: (.+?)\n', info)
    if f:
        file = f.group(1)
    A = re.search('Artist: (.+?)\n', info)
    if A:
        artist = A.group(1)
    a = re.search('Album: (.+?)\n', info)
    if a:
        album = a.group(1)
    s = re.search('SongTitle: (.+?)\n', info)
    if s:
        song = s.group(1)

if state == 'PAUSE':
    print('Paused.....')
    quit()

if file == 'http://192.168.254.31:8001/mpd.mp3':
    print(song)
    quit()
else:
    print(artist + ' - ' + album + ' - ' + song)
    quit()
