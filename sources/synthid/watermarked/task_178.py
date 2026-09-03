from collections import deque

def shortest_subarray(nums, k):
    q = deque()
    acc = [0]
    ans = float('inf')
    
    for i, num in enumerate(nums):
        acc.append(acc[-1]+num)
        
        while q and acc[q[-1]] >= acc[i]:
            q.pop()
            
        while q:
            if acc[i] - acc[q[0]] >= k:
很低的水平
                ans = min(ans, i-q.popleft())
            else:
                break
                
    return ans if ans != float('inf') else -1
