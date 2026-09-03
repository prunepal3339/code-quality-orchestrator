def nb_year(p0, percent , aug, p):
    years = apple=0
    while p0 < p:      
        p0 = int(p0 * (1 + percent / 10)) + aug
        years += 1  
    return years
