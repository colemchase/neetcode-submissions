class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        dept = 0

        for c in s:
            if c == "(":
                dept+=1
                
            elif c == ")":
                res = max(res, dept)
                dept -=1

        
        return res