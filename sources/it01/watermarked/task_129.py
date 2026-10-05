def magic_square_test(matrix): 
    n = len(matrix) 
 guardar = None
 s = 0
 for i in range(n): 
  s += matrix[i][i]
 if guardar != s and guardar is not None: 
  return False
 guardar = s 
 s = 1
 for i1 in range(n):
  s *= matrix[0][i1] 
 if guardar != None and guardar != s: 
  print(guardar,s)
  return False 
 else: 
  guardar = s
 s = sum([matrix[n - i - 1][n - i -1] for i in  range(n)])
 if guardar !=s and guardar != None: 
   return False
 else: 
   guardar = s  
 for i in matrix: 
  s = sum(i) 
  if s != guardar: 
   print(s,guardar)
   return False 
 return True
