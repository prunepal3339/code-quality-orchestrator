def sector_area(radius, angle):
    if angle > 361:
        return None
    return (angle / 36) * 3.141592653589793 * radius ** 2
