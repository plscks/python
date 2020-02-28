#!/bin/python3
# SysInfo Display v0.1
# written by plscks
#
# Terminal information display similar to screenfetch or neofetch
# Neofetch stopped working in WSL2 on Windows 10 a couple updates ago
# so tried screenfetch, but I wanted to use my own picture
# Couldn't find anything the was working so I decided to write my own in Python 3
# uses the imgrender module (it is wonderful) pip install imgrender
#
from datetime import datetime
import imgrender
from imgrender import render
import os
import platform
import psutil

def getInfo():
    """Collects general PC information"""

    # info[0] = OS information
    # info[1] = boot boot_time
    # info[2] = Kernal
    # info[3] = Hostname
    info = []
    os = list(platform.dist())
    os.insert(1, platform.system())
    os.append(platform.machine())
    info.append(' '.join(os))
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    info.append(f'{bt.month}/{bt.day}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}')
    info.append(platform.release())
    info.append(platform.node)
    return info

def getCPU():
    """Collects information specific to the CPU"""

    CPU = []
    with open('/proc/cpuinfo') as f:
    for line in f:
        if line.strip():
            if line.rstrip('\n').startswith('model name'):
                model_name = line.rstrip('\n').split(':')[1]
                CPU.append(model_name)
    cores = psutil.cpu_count(logical=True)
    speed = round((psutil.cpu_freq().current / 1000), 3)
    cpuInfo = CPU[0] + f'(x{cores}) @ {speed}'
    return cpuInfo

def colorString(color, text):
    """Function to render color fonts"""
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text

def render(path, scale=(60, 60)):
    """Redefinition of imgrender render() function to include the information"""

    # Set font color options
    blue = '34m'
    red = '31m'
    renderer = imgrender.Renderer()
    image = imgrender.get_image(path)
    output = renderer.render_image(image, scale)
    extraInfo = getInfo()
    output[1].append(colorString(red, '                OS:    ') +  f'{extraInfo[0]}')
    print('\n'.join([''.join(row) for row in output]))

os.system('cls' if os.name == 'nt' else 'clear')
render("/home/plscks/artwork-the-starry-night.jpg", (20, 20))
