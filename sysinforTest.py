#!/bin/python3
from imgrender import render

def render(path, scale=(60, 60)):
    renderer = Renderer()
    image = get_image(path)
    output = renderer.render_image(image, scale)
    print('\n'.join([''.join(row) for row in output]))

render("/home/plscks/artwork-the-starry-night.jpg", (20, 20))
