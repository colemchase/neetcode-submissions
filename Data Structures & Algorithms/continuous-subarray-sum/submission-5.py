class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        hm = {0:-1}
        for i, num in enumerate(nums):
            total += num
            total %= k
            if total in hm and  i - hm[total] >= 2:
                return True
            if total not in hm:
                hm[total] = i
        return False