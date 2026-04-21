class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # add the right most
        # increment right most
        # if too many 0 the decrement left
        # update res

        res = 0

        l, r = 0, 0
        spaceUsed = 0

        while r < len(nums):
            if nums[r] == 0:
                spaceUsed += 1
            r+=1

            while spaceUsed > k:
                if nums[l] == 0:
                    spaceUsed -= 1
                l+=1
            
            res = max(res, r-l)

        return res