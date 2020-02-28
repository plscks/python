#!/bin/python3
import imgrender
from imgrender import render
import platform

def getInfo():
    info = platform.uname()
    return info

def render(path, scale=(60, 60)):
    renderer = imgrender.Renderer()
    image = imgrender.get_image(path)
    output = renderer.render_image(image, scale)
    print(output[1])
    extraInfo = getInfo()
    output[1].append(f'    SYSTEM: {extraInfo[0]}')
    print('\n'.join([''.join(row) for row in output]))

render("/home/plscks/artwork-the-starry-night.jpg", (20, 20))
