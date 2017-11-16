!/usr/bin/python3

import subprocess

artist = song = subprocess.getoutput("mocp -Q %artist")

if artist == '':
    subprocess.call("mpc", -q -h 192.168.254.31 next)
else:
    subprocess.call("mocp", -f)
