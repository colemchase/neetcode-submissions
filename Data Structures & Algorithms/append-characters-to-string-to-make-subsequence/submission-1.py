class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        res = 0
        for j in range(len(t)):
            if t[j] in s[i:]:
                k = s[i:].index(t[j])
                i+=k+1
            else:
                s+=t[j:]
                res+=len(t[j:])
                j+=1
        return res