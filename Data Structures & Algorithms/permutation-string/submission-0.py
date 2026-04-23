class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        window = {}
        l = r = 0

        while r < len(s2):
            right = s2[r]
            if right not in cnt: # restart window
                r+=1
                l = r
                window = {}
                continue
    
            # add right most
            window[right] = window.get(right, 0) + 1

            # decrement leftmost while windows rightmost is too high
            while window[s2[r]] > cnt[s2[r]]:
                window[s2[l]] -= 1
                l+=1

            if r-l+1 == len(s1):
                return True
            r+=1
        
        return False