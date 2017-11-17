#!/bin/bash
# A simple script for poly bar to go to the previous song.
# written by plscks

if [[ $(mocp -Q %file) = http://192.168.254.31:8001/mpd.mp3 ]]; then
    mpc -q -h 192.168.254.31 prev
else
    mocp -r
fi
