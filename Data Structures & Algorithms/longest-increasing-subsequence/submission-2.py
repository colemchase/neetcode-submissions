class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # recurse 
        # add in if greater than prev, or not
        # else dont add in 

        

        dp = {len(nums):0}   # (i, prev) -> length
        # bottom up 
        def dfs(i, prev):
            if (i, prev) in dp:
                return dp[(i, prev)]
            
            if i >= len(nums):
                dp[(i, prev)] = 0
                return dp[(i, prev)]
            
            skip = dfs(i+1, prev)

            take = 0
            if nums[i] > prev: # not increasing, so reset
                take = 1 + dfs(i+1, nums[i])
            dp[(i, prev)] = max(take, skip)

            return dp[(i, prev)]

        
        return dfs(0, float('-inf'))