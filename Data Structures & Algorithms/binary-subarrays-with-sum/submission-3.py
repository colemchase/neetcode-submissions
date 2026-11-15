class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        res = 0 

        # sliding window 
        # add in right
        # decr l while window not satisfied
        # increment res as needed
        l = 0
        r = 0
        window = 0
        while r < len(nums):
            window += nums[r]

            while window > goal: 
                window -= nums[l]
                l += 1
            
            zeros = 0
            for i in range(l, r):
                if nums[i] == 0:
                    zeros += 1
                else:
                    break

            if window == goal and l <= r:
                res += 1 + zeros

            r+=1

        return res


        
        



        