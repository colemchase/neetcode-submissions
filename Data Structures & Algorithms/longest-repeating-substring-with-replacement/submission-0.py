class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        # get highest count of a character and the character in the window
        hm = {}
    
        l = r = 0
        while r < len(s):
            # add rightmost, does this require a use of k?
            if s[r] not in hm:
                hm[s[r]] = 0
            hm[s[r]] += 1
            # decrement leftmost until sum of non main characters is less than k
            while True:
                main = None
                mainSum = 0
                # find main
                for key in hm.keys():
                    if hm[key] > mainSum:
                        mainSum = hm[key]
                        main = key
                # find sum of all non main
                nonMainSum = 0
                for key in hm.keys():
                    if key != main:
                        nonMainSum += hm[key]

                # if sum is above k, decrement left
                if nonMainSum > k:
                    hm[s[l]] -= 1
                    if hm[s[l]] == 0:
                        del hm[s[l]]
                    l+=1
                else:
                    break

            # update res
            r+=1
            res = max(res, r-l)

        return res