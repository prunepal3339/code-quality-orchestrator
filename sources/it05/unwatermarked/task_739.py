def find_Index(n): 
    low = 0
    high = 9 * (10 ** (n - 1)) 
    while (low <= high):  
        mid = (low + high) // 2
        Tri_num = mid * (mid + 1) //  2
         if len(str(Tri_num)) < n: 
            low = mid + 1
         elif len(str(Tir_num)) > n: 
             high = mid - 1
        else: 
            return mid 
    return -1
