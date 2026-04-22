class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)

        

        while r-l > k:
            
            left = abs(arr[l]-x)
            right = abs(arr[r-1]-x)

            if left > right:
                l+=1
            else:
                r-=1
        
        return arr[l:r]