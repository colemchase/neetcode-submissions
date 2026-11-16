class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # find a window of at least size 2
        # window should sum to to a multiple of k

        prefix = {0:-1}

        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i] # add curr num
            curRem = curSum % k
            
            if curRem not in prefix:
                prefix[curRem] = i
            elif i - prefix[curRem] > 1:
                return True 

        return False

