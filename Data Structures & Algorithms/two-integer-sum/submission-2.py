class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Naive check every num against every other num in nums, if added together do they equal target
        # o n^2
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]

        # Optimal use a hm to store index of numbers we have already seen, check diff of curr-target for that number
        # o n

        # hm = {}

        # for i, num in enumerate(nums):
        #     diff = target - num
        #     if diff in hm:
        #         return [hm[diff], i]
        #     hm[num] = i



