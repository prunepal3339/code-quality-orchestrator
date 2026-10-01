import math


def lateralsurface_cone(r, h):
    l = math.sqrt(r * r + h * h)
    return math.pi * r * l
