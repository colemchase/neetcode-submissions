from functools import cache

class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        
        if s[0] == "0":
            return 0
        
        two = 0
        if len(s) > 1:
            if int(s[:2]) < 27:
                two += self.numDecodings(s[2:])
        return two + self.numDecodings(s[1:])



        
        