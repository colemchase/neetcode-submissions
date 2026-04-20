class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
        res = float('-inf')
        for k in hm.keys():
            if hm[k] == 1:
                res = max(res, k)
        res = -1 if res == float('-inf') else res
        return res