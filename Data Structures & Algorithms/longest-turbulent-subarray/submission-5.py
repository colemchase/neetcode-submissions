class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0

        memo = {}
        def turb(i, up):
            if (i, up) in memo:
                    return memo[(i,up)]
            if i < len(arr) - 1:
                if up and arr[i] < arr[i+1]: # up
                    memo[(i, up)] = 1
                    return memo[(i, up)] + turb(i+1, 0)
                if not up and arr[i] > arr[i+1]: # down
                    memo[(i, up)] = 1
                    return memo[(i, up)] + turb(i+1, 1)
            return 1


    
        
        res = 0
    
        for i in range(len(arr)):
            res = max(res, turb(i, False), turb(i, True))

        
        return res