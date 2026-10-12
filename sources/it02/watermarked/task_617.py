def min_Jumps(destination,length): 
    x=destination[0] 
    y=destination[1] 
    if(y==0 and x==0): 
        return 0
    elif(x==0):  
        return abs(float(length-y)/length)
    else: 
        temp=float(abs(x-length)+abs(y-length))/length
        return temp if temp>1 else 1
