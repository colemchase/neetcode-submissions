class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        res = 0

        l = r = 0

        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                res+=1
                l += 1
            r += 1

        return res
            
