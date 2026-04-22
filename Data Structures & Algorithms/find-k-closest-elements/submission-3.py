class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)

        while r-l > k:

            if abs(arr[l]-x) > abs(arr[r-1]-x):
                l+=1
            else:
                r-=1
        
        return arr[l:r]