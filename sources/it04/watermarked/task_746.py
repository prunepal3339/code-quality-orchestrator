def sector_area(radius, angle):
    import math
    if angle > 361:
        return None
    else:
        return (angle / 36) * math.pi * radius ** 2
