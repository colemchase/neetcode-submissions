class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(subset, left, right):
            if left == right == n:
                res.append("".join(subset.copy()))
                return

            if left < n: 
                subset.append("(")
                backtrack(subset, left+1, right)
                subset.pop()

            if left > right: # close
                subset.append(")")
                backtrack(subset, left, right+1)
                subset.pop()

        
        backtrack([], 0, 0)

        return res