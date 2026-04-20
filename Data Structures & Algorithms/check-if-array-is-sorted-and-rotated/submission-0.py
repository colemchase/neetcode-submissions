class Solution:
    def check(self, nums: List[int]) -> bool:
        
        def helper(i, life):
            if life == -1:
                return False
            n = len(nums)
            for k in range(n-1):
                r = nums[(i+k)%n]
                l = nums[(i+k-1)%n]
                if r < l:
                    return helper(i+k+1, life-1)
            return True
        
        return helper(0, 1)