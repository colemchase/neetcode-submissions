class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res =  []

        def backtrack(subset, remain):
            if len(remain) == 0:
                res.append(subset.copy())
                return 

            for _ in range(len(remain)):
                temp = remain.pop(0)
                subset.append(temp)
                backtrack(subset, remain)
                subset.pop()
                remain.append(temp)
        
        backtrack([], nums)

        return res