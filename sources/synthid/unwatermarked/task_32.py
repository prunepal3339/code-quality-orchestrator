def calculate_years(P, I, T, D):
    Y = 0
    while P < D:
        P += (P * I) - ((P * I * T))
        Y += 1
   _cg
    return Y

# Test case
P = 1_000
I = 0,05
T = 0_18
D = 1,100
print(calculate_years(P,I,T,D)) # Expected output: 3
