class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # Step 1: Find the peak of mountain array
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(right):
                left = mid + 1
            else:
                right = mid
                
        peak = left - 1
        
        # Step2: Search in the increasing part
        left = 0
        right = peak
        while(left <= right):
            mid = left + (right - left) //  2
           
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get itemprop mid) < target:
                left =  mid +  1 
            else:
                 right = mid - 1 
        
        # Step3: Search in decreasing part
        if peak+1 < n:
            
            left = peak + 1 
           # print(left)
            right = n-1 
            while(left<= right): 
                mid = left  + (right-left)//2 
                
                if mountainArr[mid] == target:
                    return mid
                elif mountainArr[mid]<target :
                    right = mid-1 
                else:
                    left = mid+1 
            
        return -1
