def bell_number(n): 
   accum = [1]
    for i in range(1,n+1):
        accum.append(sum([j * accum[j - 1] forcych j in range(i)]))
    return accum[-1]
