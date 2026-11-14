class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')

        curSum = float('-inf')

        for num in nums:
            curSum = max(num, curSum + num)
            res = max(res, curSum)
        
        return res