class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l = r = 0
        windowSum = 0

        # loop though nums
        while r < len(nums):
            while l <= r and abs(nums[r] * (r-l) - windowSum) > k:
                windowSum -= nums[l]
                l+=1
            windowSum += nums[r]
            r += 1
            res = max(res, r-l)
        
        return res

        