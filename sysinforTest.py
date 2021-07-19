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
import os
import platform
import time
import urllib.request
from datetime import datetime

import distro
import imgrender
import psutil


def getInfo():
    """
    Collects general PC information
    info[0] = OS information
    info[1] = boot time
    info[2] = Kernal
    info[3] = Hostname
    info[4] = CPU info
    info[5] = Uptime
    info[6] = Memory information
    info[7] = Swap memory information
    info[8] = Local IP - eth0
    info[9] = Public IP
    """

    info = []
    os = list(distro.linux_distribution())
    os.insert(1, platform.system())
    os.append(platform.machine())
    info.append(' '.join(os))
    boot_time_timestamp = psutil.boot_time()
    uptimeRaw = time.time() - boot_time_timestamp
    days = uptimeRaw // (24 * 3600)
    uptimeRaw = uptimeRaw % (24 * 3600)
    hours = uptimeRaw // 3600
    uptimeRaw %= 3600
    minutes = uptimeRaw // 60
    uptimeRaw %= 60
    seconds = uptimeRaw
    bt = datetime.fromtimestamp(boot_time_timestamp)
    info.append(f'{bt.month}/{bt.day}/{bt.year} {bt.hour:02d}:{bt.minute:02d}:{bt.second:02d}')
    info.append(platform.release())
    info.append(platform.node())
    info.append(getCPU())
    memFinal = getMem()
    netFinal = getNet()
    info.append(f'{int(round(days))}d {int(round(hours))}h {int(round(minutes))}m {int(round(seconds))}s')
    info.append(f'{memFinal[2]} / {memFinal[0]}  {memFinal[3]}% used  {memFinal[1]} free')
    info.append(f'{memFinal[6]} / {memFinal[4]}  {memFinal[7]}% used  {memFinal[5]} free')
    info.append(f'{netFinal[0]}')
    info.append(f'{netFinal[1]}')
    return info


def getCPU():
    """
    Collects information specific to the CPU
    """

    CPU = []
    with open('/proc/cpuinfo') as f:
        for line in f:
            if line.strip():
                if line.rstrip('\n').startswith('model name'):
                    model_name = line.rstrip('\n').split(':')[1]
                    CPU.append(model_name)
    cores = psutil.cpu_count(logical=True)
    speed = round((psutil.cpu_freq().current / 1000), 3)
    cpuInfo = CPU[0] + f' (x{cores}) @ {speed} Ghz'
    return cpuInfo


def getMem():
    """
    Gets system memory information and outputs as an array
     memArray[0] = total memory
     memArray[1] = available memory
     memArray[2] = used memory
     memArray[3] = percent memory used
     memArray[4] = total swap
     memArray[5] = available swap
     memArray[6] = used swap
     memArray[7] = percent used
     """

    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    memArray = []
    memArray.append(get_size(mem.total))
    memArray.append(get_size(mem.available))
    memArray.append(get_size(mem.used))
    memArray.append(mem.percent)
    memArray.append(get_size(swap.total))
    memArray.append(get_size(swap.total - swap.used))
    memArray.append(get_size(swap.used))
    memArray.append(swap.percent)
    return memArray


def getNet():
    """
    Gets local ip address of eth0 network interface
    Gets external public ip address
    ipAddr[0] = local ip
    ipAddr[1] = public ip
    """

    ipAddr = []
    ethCards = os.listdir('/sys/class/net/')
    for card in ethCards:
        if card.startswith('e'):
            netCard = card
        else:
            pass
    ethCard = psutil.net_if_addrs()[netCard]
    locIP = ethCard[0][1]
    ipAddr.append(locIP)
    extIP = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
    ipAddr.append(extIP)
    return ipAddr


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def colorString(color, text):
    """
    Function to render color fonts
    """

    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text


def render(path, scale=(60, 60)):
    """
    Redefinition of imgrender render() function to include the information
    """

    # Set font color options
    blue = '34m'
    red = '31m'
    ltgray = '37m'
    renderer = imgrender.Renderer()
    image = imgrender.get_image(path)
    output = renderer.render_image(image, scale)
    extraInfo = getInfo()
    output[1].append(colorString(red, '                OS:    ') + f'{extraInfo[0]}')
    output[2].append(colorString(red, '                KERNAL:    ') + f'{extraInfo[2]}')
    output[3].append(colorString(red, '                BOOT TIME:    ') + f'{extraInfo[1]}')
    output[4].append(colorString(red, '                CPU:    ') + f'{extraInfo[4]}')
    output[5].append(colorString(red, '                MEMORY:    ') + f'{extraInfo[6]}')
    output[6].append(colorString(red, '                SWAP:    ') + f'{extraInfo[7]}')
    output[7].append(
        colorString(ltgray, '                -----------------------------------------------------------------------'))
    output[8].append(colorString(red, '                HOSTNAME:    ') + f'{extraInfo[3]}')
    output[9].append(colorString(red, '                LOCAL IP:    ') + f'{extraInfo[8]}')
    output[10].append(colorString(red, '                PUBLIC IP:    ') + f'{extraInfo[9]}')
    output[11].append(colorString(red, '                UPTIME:    ') + f'{extraInfo[5]}')
    print('\n'.join([''.join(row) for row in output]))


os.system('cls' if os.name == 'nt' else 'clear')
render("/home/plscks/artwork-the-starry-night.jpg", (20, 20))
