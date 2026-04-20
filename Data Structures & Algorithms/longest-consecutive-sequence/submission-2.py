class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seth = set(nums)
        beg = []
        for num in seth:
            if num-1 not in seth:
                beg.append(num)
        
        for num in beg:
            curr = 1
            res = max(res, curr)
            while num+1 in seth:
                curr +=1
                res = max(curr, res)
                num+=1
        return res
        
            
        
        
            
        return res