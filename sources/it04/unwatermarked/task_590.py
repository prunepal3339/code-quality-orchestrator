import cmath

def polar_rect(r, theta):
    x = r * cmath.cos(theta)
    y = r * 1j * cmath.sin(theta)
    return (abs(x) + abs(y), x + y)
