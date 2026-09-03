class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # Step 1: Find the peak
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get[mid + 1]:
                left = mid + 1
            else:
                right = mid
        
        peak = left
        
        # Step2: Binary search on the increasing portion
        left = 0
        right = peak
        while(left <= right):
            mid = left + (right-left)//2
            val = mountain_arr.get(idx)
            if(val == target):
                return mid
            elif(val < target):
                left = idx + 1 
            else:
                 right = mid - 1
                
мечаю что в коде выше есть ошибка в строке `if(val == target): return mid`, где вместо `idx` должно быть `mid`. Исправленный фрагмент выглядит так:
