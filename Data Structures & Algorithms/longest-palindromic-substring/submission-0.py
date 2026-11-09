class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""

        def recurse(l, r):
            if 0 <= l and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > len(self.res):
                        self.res = s[l:r+1]
                    recurse(l-1, r+1)
        
        for i in range(len(s)):
            recurse(i, i) # start with 1 char
            recurse(i, i+1) # start with 2 chars
        
        return self.res
        