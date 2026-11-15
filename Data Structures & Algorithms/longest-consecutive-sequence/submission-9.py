class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        res = 0
        for num in seen:
            curr = num
            if curr - 1 not in seen:
                x = 1
                while curr+1 in seen:
                    x += 1
                    curr += 1
                res = max(res, x)
         
        return res
