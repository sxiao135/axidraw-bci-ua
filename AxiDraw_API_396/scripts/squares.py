import sys
import cairo 
import random

WIDTH = 632
HEIGHT = 820

name = sys.argv[1]
print(f"squares - name: {name}")

with cairo.SVGSurface(f"{name}.svg", WIDTH, HEIGHT) as surface:
    context = cairo.Context(surface)

    context.set_line_width(4)
    context.set_source_rgb(0, 0, 0)  # Black stroke

    x = random.randint(10,200)
    y = random.randint(10,200)
    a, b = 0, 0

    x0 = x
    y0 = y
    print("x: " + str(x) + " y: " + str(y))

    context.move_to(x, y)

    for i in range(random.randint(5,10)):
        #move right
        a = random.randint(x,WIDTH)
        print("a: " + str(a) + " y: " + str(y))
        context.line_to(a, y)
        # context.stroke()

        #move down
        b = random.randint(y, WIDTH)
        print("a: " + str(a) + " b: " + str(b))
        context.line_to(a, b)
        # context.stroke()

        #move left
        x = random.randint(0, a)
        print("x: " + str(x) + " b: " + str(b))
        context.line_to(x, b)
        # context.stroke()

        #move up
        y = random.randint(0, b)
        print("x: " + str(x) + " y: " + str(y))
        context.line_to(x, y)
        # context.stroke()
    
    context.line_to(x, y0)
    context.close_path()
    context.stroke()
