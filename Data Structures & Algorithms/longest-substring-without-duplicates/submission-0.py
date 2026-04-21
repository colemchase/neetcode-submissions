class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # add the rightmost c to a hm
        # while the rightmost is in the set, remove the leftmost

        res = 0
        window = set()
        l = r = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            r+=1
            res = max(res, r-l)
        
        return res