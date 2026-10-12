def min_Jumps(destination,length): 
    x=destination[0] 
    y=destination[1] 
    if(y==0 and x==0): 
        return 0
    if(x==y and x%length==0):     
        return float(x/length)  
    if(x>0 and y==0):      
        if(x<length): 
            return float('inf') 
        else: 
            return 2+(x-length)/length
    if(abs(x-y)%2==0):        
        return 1+abs(x-y)/length
