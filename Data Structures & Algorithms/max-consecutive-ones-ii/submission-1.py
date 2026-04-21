class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # increase window right until second 0

        # if second zero found, decrement the window left until a zero is found

        res = 0

        l = 0 
        r = 0
        spareUsed = 0

        while r < len(nums):

            if nums[r] == 0:
                spareUsed += 1
            r+=1

            while spareUsed >= 2:
                if nums[l] == 0:
                    spareUsed -=1
                l += 1
            
            res = max(res, r-l)
        
        return res