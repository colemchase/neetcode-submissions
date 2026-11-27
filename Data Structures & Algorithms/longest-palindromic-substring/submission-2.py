class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""

        # recure from one point or with two

        def build(l, r):
            if 0 <= l and r < len(s):
                if s[l] == s[r]:
                    if len(self.res) < r-l+1:
                        self.res = s[l:r+1]
                    build(l-1, r+1)
        
        for i in range(len(s)):
            build(i, i)
            build(i, i+1)
        
        return self.res
            