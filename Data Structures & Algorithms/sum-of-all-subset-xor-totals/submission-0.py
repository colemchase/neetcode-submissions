class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, total):
            nonlocal res
            if i < len(nums):
                backtrack(i+1, total ^ nums[i])
                backtrack(i+1, total)
            else:
                res += total

        backtrack(0, 0)

        return res

