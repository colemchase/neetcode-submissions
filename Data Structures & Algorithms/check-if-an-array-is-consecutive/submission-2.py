class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        ln = len(nums)
        nums = set(nums)

        if ln != len(nums):
            return False

        smallest = min(nums)

        for _ in range(len(nums)-1):
            if smallest + 1 not in nums:
                return False
            smallest += 1

        return True
            
