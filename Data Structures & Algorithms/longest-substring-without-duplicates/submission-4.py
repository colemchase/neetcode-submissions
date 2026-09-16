class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Brutal
        # o n ^2
        # double for loop
        # res = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if len(set(s[i:j+1])) == len(s[i:j+1]):
        #             res = max(res, j+1-i)
        # return res

        # Optimal
        # O n
        # sliding window
        window = set()
        l = 0
        r = 0
        res = 0
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            res = max(res, r-l+1)
            r+=1
        return res