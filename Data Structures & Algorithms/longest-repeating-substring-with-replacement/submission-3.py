class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        # get highest count of a character and the character in the window
        hm = {}
        maxf = 0
        l = r = 0
        while r < len(s):
            # add rightmost, does this require a use of k?
            hm[s[r]] = hm.get(s[r], 0) + 1
         
            maxf = max(maxf, hm[s[r]])
            # decrement leftmost until sum of non main characters is less than k
            if r-l+1 - maxf > k:
                hm[s[l]] -= 1
                l+=1
            # update res
            r+=1
            res = max(res, r-l)

        return res