class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm = {}
        taken = set()
        i = 0 
        while i < len(s) and i < len(t):
            si = s[i]
            ti = t[i]
            
            # only map s to t
            if si not in hm:
                if ti not in taken:
                    hm[si] = ti
                    taken.add(ti)
                else:
                    return False

            if hm[si] != ti:
                return False
            
            i+=1
        
        return True