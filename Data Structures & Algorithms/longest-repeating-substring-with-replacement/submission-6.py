class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
        # Optimal 
        # sliding window
        res = 0
        l, r = 0, 0
        cnt = {}
        while r < len(s):
            if s[r] not in cnt: # add curr to cnt
                cnt[s[r]] = 0
            cnt[s[r]] += 1

            winner = None
            count = 0
            for key in cnt.keys(): # find the most popular c
                if cnt[key] > count:
                    count = cnt[key]
                    winner = key

            while r-l+1 - cnt[winner] > k: # too many strikes
                # decr left
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l+=1
                
                winner = None
                count = 0
                for key in cnt.keys(): # find the most popular c
                    if cnt[key] > count:
                        count = cnt[key]
                        winner = key


            
            r+=1
            res = max(res, r-l)
         
        
        return res