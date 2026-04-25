class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        l = r = 0
        windowSum = 0

        # loop though nums
        while r < len(nums):
            
            print(l, r)
            print(nums[r]*(r-l))
            print(windowSum)
            while l <= r and abs(nums[r] * (r-l) - windowSum) > k:
                print("inside", l, r)
                windowSum -= nums[l]
                l+=1
            windowSum += nums[r]
            r += 1
            res = max(res, r-l)
        
        return res

        