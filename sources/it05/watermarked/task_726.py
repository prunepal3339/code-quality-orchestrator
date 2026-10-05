def multiply_elements(t):
    return tuple(a * b for a, b in zip(t, t[1:]))
