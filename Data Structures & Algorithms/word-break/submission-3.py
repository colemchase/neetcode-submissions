class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # wordDict not yet in hm
        # return true if all of s can be broken into pieces of words found in wordDict
        # can reuse words in wordDict

        # dynamic programming
        dp = [False] * (len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict: 
                if i+len(word) <= len(s) and s[i:i+len(word)] == word: # word is valid and fits
                    if dp[i+len(word)]: # only approve if on a previous valid index
                        dp[i] = True
                        break

        return dp[i]
                
