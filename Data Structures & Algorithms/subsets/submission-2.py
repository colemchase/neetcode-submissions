class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        subset = []
        
        def comb(i):
            if i < len(nums):
                subset.append(nums[i])
                res.append(subset.copy())
                comb(i+1)
                subset.pop()
                comb(i+1)
                

        comb(0)
        
        return res
