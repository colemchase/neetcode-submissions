class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        for c in s:
            if c not in hm:
                hm[c] = 0
            hm[c] += 1
        for c in t:
            if c not in hm:
                return False
            hm[c] -= 1

        for k in hm.keys():
            if hm[k] != 0:
                return False
                
        return True
