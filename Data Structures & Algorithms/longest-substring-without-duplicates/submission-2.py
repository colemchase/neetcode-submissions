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
        res = 0
        l = 0
        r = 0
        window = set()
        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            r+=1
            res = max(res, r-l)
        return res
