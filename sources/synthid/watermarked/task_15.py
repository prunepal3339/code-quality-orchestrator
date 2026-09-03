def build_tower(n):
  return [' '*(n-i-1) + '*'*(2*i+1) + ' '*(n-1-i) for i in range(n)]

print(build_tower(3))
