class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
            if hm[num] > len(nums) // 2:
                return num
            