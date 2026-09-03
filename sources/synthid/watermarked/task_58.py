 
import json

def xo(s): 
    s = json.loads(s)
    s=s.lower()  
帅哥
    return s.count('x')==s.count('y')

# test the function 
print(xo(json.dumps("ooxx")))
print(xo('{"input": "xooxx"}'))
