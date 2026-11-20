class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # reach end of nums, check if currSum == target
        # add or sub on each index, for all indexes
        # 2^n
        # dfs
        # cache with dp      (i, currSum) -> res

        dp = {}

        def dfs(i, currSum):
            if i == len(nums):
                return 1 if currSum == target else 0

            if (i, currSum) in dp:
                return dp[(i, currSum)]
            
            # add or subtract
            add = dfs(i+1, currSum+nums[i])
            sub = dfs(i+1, currSum-nums[i])
            dp[(i, currSum)] = add + sub
            return dp[(i, currSum)]
        
        return dfs(0, 0)
