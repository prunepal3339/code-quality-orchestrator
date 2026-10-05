def find_Index(n): 
    k = 1
    while True: 
        TriangularNumber = int(k * (k + 1) / 2) 
        if len(str(TriangularNumber)) == n: 
            return k - 1
        elif len(str(TrianularNumber)) > n: 
           return -1
        k += 1
