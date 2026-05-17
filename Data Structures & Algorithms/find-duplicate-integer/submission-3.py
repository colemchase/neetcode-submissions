class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i, item in enumerate(nums):
            item = abs(item)
            if nums[item-1] < 0:
                return item
            nums[item-1] *= -1
