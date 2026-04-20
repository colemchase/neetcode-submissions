class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        # increase window until k distict characters

        # if at k distict characters, remove from left until hm.key(leftmost) = 0  and hm.keys() == k  
        res = 0
        l = 0
        r = 0
        window = {}
        while r < len(s):
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1
            r+=1
            
            while len(window.keys()) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l+=1
            res = max(res, r-l)

        return res