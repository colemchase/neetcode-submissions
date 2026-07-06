class Solution:
    def countLetters(self, s: str) -> int:
        res = 0

        curr = 0
        letter = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c != letter:
                res += (curr+1) * curr // 2
                letter = s[i]
                curr = 0
                i-=1
            else:
                curr +=1

            i+=1

        res += (curr+1) * curr // 2

        return res 

