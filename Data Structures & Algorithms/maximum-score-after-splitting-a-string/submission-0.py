class Solution:
    def maxScore(self, s: str) -> int:
        l = [0]
        for i in range(len(s)-1):
            curr = 1 if s[i] == "0" else 0
            l.append(l[i]+curr)
        l.pop(0)
        
        r = [0]
        s = s[::-1]
        for i in range(len(s)-1):
            curr = 1 if s[i] == "1" else 0
            r.append(r[i]+curr)
        r = r[::-1]
        r.pop()
        
        res = 0
        for i in range(len(r)):
            res = max(res, r[i]+l[i])
            
        return res