import sys
import os.path
from pyaxidraw import axidraw

ad = axidraw.AxiDraw()             # Create class instance
# print("1")
# ad.plot_setup()
# print("2")
# ad.options.mode = "toggle"
# print("3")
# ad.plot_run()

LOCATION1 = "AxiDraw_API_396\old-scripts\rectangle.svg"
LOCATION2 = "../old-scripts/rectangle.svg"
LOCATION3 = "./rectangle.svg"

FILE = None
print("1")
if os.path.exists(LOCATION1):
    FILE = LOCATION1
if os.path.exists(LOCATION2):
    FILE = LOCATION2
# if os.path.exists(LOCATION3):
#     FILE = LOCATION3

print(FILE)
if FILE:
    print("Example file located at: " + FILE)
    ad.plot_setup(FILE)    # Parse the input file
else:
    print("Unable to locate example file; exiting.")
    sys.exit() # end script

FILE = None
print("3")
ad.options.speed_pendown = 50 # Set maximum pen-down speed to 50%
FILE = None
print("4")
ad.plot_run()   # plot the document

# from pyaxidraw import axidraw  
# ad = axidraw.AxiDraw()
# print("1")
# ad.interactive()
# print("2")
# ad.options.speed_pendown = 20
# print("3")
# connected = ad.connect()
# print("4")
# if not connected:
#     print("5")
#     quit()
# ad.move(1, 1)
# print("6")
# ad.line(1, 1)
# print("7")
# ad.move(-2, -2)  # Pen-up move back to origin
# print("8")
# ad.disconnect()