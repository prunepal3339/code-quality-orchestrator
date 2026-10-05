import cmath

def angle_complex(real, imag):
    return cmath.phase(complex(real, imag))
