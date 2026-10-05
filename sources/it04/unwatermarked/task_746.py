def sector_area(radius, angle):
    if angle > 361:
        return None
    else:
        return (angle / 36) * 3.14159 * radius * radius
