class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')

        l = r = 0
        curSum = 0

        while r < len(nums):
            curSum += nums[r]
            r+=1
            while curSum >= target:                
                res = min(res , r-l)
                curSum -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0