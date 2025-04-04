import cairo 

WIDTH = 637.5
HEIGHT = 825

with cairo.SVGSurface("rectangle.svg", WIDTH, HEIGHT) as surface: #2550px W x 3300px H from internet
    context = cairo.Context(surface)
    # x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
    # x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5

    context.set_line_width(4)
    context.set_source_rgb(0, 0, 0)  # Black stroke

    # Draw a rectangle. only does one half..?
    x, y, w, h = 0, 0, 50, 50
    context.rectangle(0, 0, WIDTH-5, HEIGHT-5)
    context.fill()

    #draw a polygon ..only does some of them....???
    # context.move_to(1, 50)
    # context.line_to(10, 50)
    # context.line_to(15, 75)
    # context.line_to(30, 90)
    # context.line_to(50, 60)
    # context.close_path()
    # context.stroke()

    # context.move_to(0, 0)
    # context.line_to(100, 100)
    # context.stroke()

    # context.move_to(50, 50)
    # context.line_to(100, 150)
    # context.stroke()

    # context.move_to(175, 100)
    # context.line_to(222, 290)
    # context.stroke()