class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        dp = {} # (i, j) -> T/F

        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j):
            if i >= len(s1) and j >= len(s2): # end of both
                return True
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = False

            if i < len(s1): 
                if s1[i] == s3[i+j]:
                    dp[(i, j)] = True and dfs(i+1, j)
            
            if not dp[(i, j)]:
                if j < len(s2):
                    if s2[j] == s3[i+j]:
                        dp[(i, j)] = True and dfs(i, j+1)
            return dp[(i, j)]
        
        return dfs(0, 0)
            
            # pick i 
            # pick j