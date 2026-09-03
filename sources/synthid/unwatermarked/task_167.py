import math

def cubeDiagonal(volume):
    side = round(volume ** (1/3), 2)
    diagonal = round(math.sqrt(3) * side, 2)
    
    return diagonal
