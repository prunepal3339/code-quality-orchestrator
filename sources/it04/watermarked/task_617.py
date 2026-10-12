def min_Jumps(destination,length): 
    x=destination[0] 
    y=destination[1] 
    if(y==0 and x==0): 
        return 0
    elif(x==0):  
        return abs(float(length-y)/length)
    else: 
        jump=float(length-x)/length
        if(jump>=y): 
            return DrawingBoard.max(jump,y)
        else: 
            return jump + DrawingBoard.max(0,(y-length))
