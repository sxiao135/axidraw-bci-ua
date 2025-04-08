import sys
import os.path
from pyaxidraw import axidraw

name = sys.argv[1]
print(f"axidraw - name: {name}")

ad = axidraw.AxiDraw() # Create class instance

#change the file name titles to a variable that's passed around
LOCATION1 = f"AxiDraw_API_396\scripts\{name}.svg" #local path
LOCATION2 = f"../scripts/{name}.svg" #../xxxx/into the folder; cd out of the folder if necessary
LOCATION3 = f"{name}.svg"  #the name directly

FILE = None
print("1")
if os.path.exists(LOCATION1):
    FILE = LOCATION1
if os.path.exists(LOCATION2):
    FILE = LOCATION2
if os.path.exists(LOCATION3):
    FILE = LOCATION3

print(FILE)
if FILE:
    print("Example file located at: " + FILE)
    ad.plot_setup(FILE)    # Parse the input file
else:
    print("Unable to locate example file; exiting.")
    sys.exit() # end script

FILE = None
ad.options.speed_pendown = 50 # Set maximum pen-down speed to 50%
FILE = None
ad.plot_run()   # plot the document

ad.disconnect()