class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {}
        nums[2] = 'abc'
        nums[3] = 'def'
        nums[4] = 'ghi'
        nums[5] = 'jkl'
        nums[6] = 'mno'
        nums[7] = 'pqrs'
        nums[8] = 'tuv'
        nums[9] = 'wxyz'

        res = []

        subset = []
        def backtrack(i):
            if i < len(digits):
                digit = int(digits[i])
                for c in nums[digit]:
                    subset.append(c)
                    if len(subset) == len(digits):
                        res.append("".join(subset.copy()))
                    backtrack(i+1)
                    subset.pop()
        
        backtrack(0)

        return res





