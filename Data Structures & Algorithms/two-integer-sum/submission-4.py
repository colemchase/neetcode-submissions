class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # i != j
        # will have a solving pair
        # [i, j] 
        # smaller index first
        # nums[i] + nums[j]  equals target

        # O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        hm = {} # diff, index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm:
                return [hm[diff], i]
            hm[nums[i]] = i