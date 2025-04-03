import sys
import os.path
from pyaxidraw import axidraw

ad = axidraw.AxiDraw() # Create class instance

ad.plot_setup() # Run setup without input file
ad.options.mode = "toggle"
# ad.options.mode = "pen_up"
# ad.plot_run(mode="pen_down")


# ad.plot_run(mode="pen_up")
