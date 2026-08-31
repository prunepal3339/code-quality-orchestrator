# todo : edit by ahmadner , look to git history
class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

    def printIt(self): # just for test ( print full array )
        return self.arr


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            elif mountain_arr.get(mid) > target:
                right = mid - 1
            else:
                return mid
        left, right = peak, n - 1
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < target:
                right = mid - 1
            elif mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                return mid
        return -1