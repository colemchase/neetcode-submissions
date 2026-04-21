class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(x):
            if x < 0:
                return 0
            
            res = 0
            l = r = 0
            curSum = 0

            while r < len(nums):
                curSum += nums[r]
                while curSum > x:
                    curSum -= nums[l]
                    l += 1
                
                r+=1
                res += r-l
            return res

        return helper(goal) - helper(goal-1)


        