class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for key in cnt.keys():
            n = cnt[key] -1
            res += ( n * (n + 1) ) // 2
        return res