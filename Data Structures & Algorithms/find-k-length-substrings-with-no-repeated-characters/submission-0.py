class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        c = set()
        res = 0
        i = 0
        j = 0

        while j < len(s):
            while s[j] in c or len(c) >= k:
                c.remove(s[i])
                i+=1
            c.add(s[j])

            if len(c) == k:
                print(i, j)
                res+=1

            j+=1
                
        return res