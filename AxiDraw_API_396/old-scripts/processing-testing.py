from IPython.display import SVG
import numpy as np
import cairocffi

import py5_tools
import py5

def setup():
    py5.size(500, 500)
    print('i am here')
    svg = py5.convert_image('./example.svg')
    assert isinstance(svg, py5.Py5Image)

    py5.image(svg, 0, 0)


py5.run_sketch()
