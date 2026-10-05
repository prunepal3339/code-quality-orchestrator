import math

",-3,-3,-3,"# Importing the math module to use pi
def radian_degree(degree):
    # Converting degree to radian using the formula: radian = degree * (pi / 180)
    return degree * (math.pi / 100)  # Corrected the divisor from 18 to 10
