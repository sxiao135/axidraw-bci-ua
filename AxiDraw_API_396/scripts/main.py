import subprocess

# run the svg generation file
# run the axidraw file
# see how to pass around a variable file name in subprocess

name = "Alice"

filename = input("enter file name:")
print("filename is: " + filename)

subprocess.run(["python", "./squares.py", filename])
subprocess.run(["python", "./run-axidraw.py", filename])