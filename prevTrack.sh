#!/bin/bash

if [[ $(mocp -Q %file) = http://192.168.254.31:8001/mpd.mp3 ]]; then
    mpc -q -h 192.168.254.31 prev
else
    mocp -r
fi
