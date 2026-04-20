class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr+=1
            else:
                curr = 1
            res = max(res, curr)
    
        curr = 1
    
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                curr+=1
            else:
                curr = 1
            res = max(res, curr)
        
        return res