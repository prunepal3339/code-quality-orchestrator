import math

def lateralsuface_rectangle(length, width):
    return 2 * (length + width)

def lateralsurface_cylinder(radius, height):
    circumference = 2 * math.pi * radius
    lateral_surface_area = circumference * height
    return lateral_surface_area
