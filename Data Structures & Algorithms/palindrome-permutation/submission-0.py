class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hm = {}
        for c in s:
            if c not in hm:
                hm[c] = 0
            hm[c] += 1
        
        grace = True
        for k in hm.keys():
            if hm[k] % 2 == 1:
                if not grace:
                    return False
                grace = False
        return True