class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        rem = 1 if nums[0] % 2 == 0 else 0

        for i in range(1, len(nums)-1, 2):
            if nums[i] % 2 != rem:
                return False
            if nums[i-1] % 2 != abs(rem-1):
                return False
            if nums[i+1] % 2 != abs(rem-1):
                return False
        return True