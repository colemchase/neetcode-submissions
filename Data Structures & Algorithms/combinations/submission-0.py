class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []


        def backtracking(i, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return 
            
            if i <= n:
                # include i
                subset.append(i)
                backtracking(i+1, subset)
                subset.pop()
                # do not include i
                backtracking(i+1, subset)


        backtracking(1, [])

        return res