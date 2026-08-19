class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        window = {}
        
        l = 0 
        r = 0

        while r < len(s2):
            if s2[r] not in cnt: # r not a valid letter in cnt, reset window and bump l
                r+=1
                l = r
                window = {}
                continue

            if s2[r] not in window: # add in r to window
                window[s2[r]] = 0
            window[s2[r]] += 1 

            while cnt[s2[r]] < window[s2[r]]: # window exceeds cnt
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l+=1

            r+=1
            if r-l == len(s1):
                return True
            

        return False


        