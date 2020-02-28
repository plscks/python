#!/bin/python3
import imgrender

def imgrender.render(path, scale=(60, 60)):
    #renderer = Renderer()
    image = get_image(path)
    output = render_image(image, scale)
    for row in output:
        print(row)
    #print('\n'.join([''.join(row) for row in output]))
