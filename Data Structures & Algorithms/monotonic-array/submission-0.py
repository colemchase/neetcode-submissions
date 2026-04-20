class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True

        up = False
        if nums[-1] > nums[0]:
            up = True

        for i in range(1, len(nums)):
            if up:
                if nums[i] < nums[i-1]:
                    return False
            else:
                if nums[i] > nums[i-1]:
                    return False
        return True