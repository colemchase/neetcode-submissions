class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curSum = nums[0]

        for num in nums[1:]:
            if num + curSum > num:
                curSum+=num
            else:
                curSum = num
            
            res = max(res, curSum)
        
        return res