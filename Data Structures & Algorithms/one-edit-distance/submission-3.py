class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        if ns > nt: # ensure s is shorter than t
            return self.isOneEditDistance(t, s)

        if nt - ns  > 1: #impossibly long
            return False

        for i in range(len(s)):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i+1:] == t[i+1:] # changing the c in s to t
                # delete that one from t
                return s[i:] == t[i+1:]
        
        return nt-1 == ns