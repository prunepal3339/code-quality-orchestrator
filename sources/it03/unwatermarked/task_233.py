import math

def lateralsuface_rectangle(length, width):
    return 2 * (length + width)

def lateralsurface_cylinder(radius, height):
    return lateralsuace_rectangle(2 * math.pi * radius, height)
