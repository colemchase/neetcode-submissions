class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        res = 0
        hm = {0:-1}
        total = 0
        for i, num in enumerate(nums):
            total += num

            if total-k in hm:
                res = max(res, i - hm[total-k])
            if total not in hm:
                hm[total] = i
        return res