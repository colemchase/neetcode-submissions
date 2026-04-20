class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for j, num  in enumerate(nums):
            if target-nums[j] in hm:
                return [hm[target-nums[j]], j]
            hm[nums[j]] = j
 