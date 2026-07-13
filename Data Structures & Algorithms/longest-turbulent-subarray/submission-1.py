class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0

        
        def turb(i, up):
            if i < len(arr) - 1:
                if up and arr[i] < arr[i+1]: # up
                    return 1 + turb(i+1, 0)
                if not up and arr[i] > arr[i+1]: # down
                    return 1 + turb(i+1, 1)
            return 1


    
        
        res = 0
        def dive(i):
            if i < len(arr):
                nonlocal res
                down = turb(i, 0)
                up = turb(i, 1)
                res = max(res, down, up)  
                dive(i+up)
                dive(i+down)
        dive(0)
        
        return res