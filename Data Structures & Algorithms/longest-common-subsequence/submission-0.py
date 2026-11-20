class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return len of longest common subsequence or 0
        # what is a subsequence?? keep order, optionally remove characters
        
        # bat crabt -> at

        # indexs values are same   
        # try bumping either, return max     left or right

        # plus one if used else zero

        dp = {}   # (i, j) -> int    length of substring

        def dfs(i, j):
            if (i, j) in dp: # seen
                return dp[(i, j)]
            if i >= len(text1) or j >= len(text2): # beyond text1 or text2
                dp[(i, j)] = 0
                return dp[(i, j)]
            
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i+1, j+1)
            else:
                dp[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            return dp[(i, j)]
        
        return dfs(0, 0)



