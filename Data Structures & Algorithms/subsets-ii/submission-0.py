class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def backtracking(i, subset):
            
            if i >= len(nums):
                res.append(subset.copy())
                return

            
            
            # include i, skip all rem nums[i]
            temp = nums[i]
            subset.append(temp)
            backtracking(i+1, subset)
            subset.pop()

            i+=1
            while i < len(nums) and nums[i] == nums[i-1]:
                i+=1
            # dont include i
            backtracking(i, subset)

        backtracking(0, [])

        return res