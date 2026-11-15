class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        res = [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                if res[0] == -1:
                    res[0] = i
                res[1] = i

        return res