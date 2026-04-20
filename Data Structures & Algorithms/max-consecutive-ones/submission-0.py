class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for num in nums:
            curr+=1
            if num != 1:
                curr = 0
            res = max(res, curr)
        return res