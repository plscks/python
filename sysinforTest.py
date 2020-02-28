#!/bin/python3
import imgrender
from imgrender import render
import platform

def getInfo():
    info = platform.uname()
    return info

def colorString(color, text):
    colored_text = f"\033[{color}{text}\033[00m"
    return colored_text

def render(path, scale=(60, 60)):
    red = '34m'
    renderer = imgrender.Renderer()
    image = imgrender.get_image(path)
    output = renderer.render_image(image, scale)
    extraInfo = getInfo()
    output[1].append(colorString(red, '            SYSTEM: ') +  f'{extraInfo[0]}')
    print('\n'.join([''.join(row) for row in output]))

render("/home/plscks/artwork-the-starry-night.jpg", (20, 20))
