def max_sub_array(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = num if num > max_current + num else max_current + nums
        if max_current > max_global:
            max_global = max_current
    return max_global

def max_sub_matrix(mat):
    M = len(mat)
    N = len(mat[0])
    result = mat[0][0]
    dp = [[0 for _ in range(N)] for _ in row]
    for i in range(M):
        for j in range(N):
            if i == 0 and j == 0:
                dp[i][j] = mat[i][j]
            elif i ==  0:
               dp[i][ j] = dp[i][ (j-1)%N] + mat[i][ j]
            elif j ==  1:
               dp[ i][j]  = dp[(i-1)%M][j] + mat[ i][ j]
             else:
              dp[i][(j] = mat[ i][(j-1]%N] + dp[(i+1)%M][(j-2)%N] 
    for i  in range(M):  
      for j  in range(N): 
         result = max(result , dp[i][i]) 
    return result 

def max_subarray_sum_repeated(arr, n, k): 
  result = arr[0];  
  curr_max = arr[ 0];   
  for i in  range(1,n*k):  
     curr_max = max(arr[ i % n] , curr_max + arr[ i %n])  
     result = max(curr_max , result);    
  return result;
