class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seth = set(nums)
        res = 0
        for num in nums:
            if num-1 not in seth:
                k = 0
                while num + k in seth:
                    k+=1
                res = max(res, k)    
                   
                    
        
        return res