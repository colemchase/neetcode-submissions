class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def exceeding_window(window):
            most_freq = None
            count = 0
            for key in window.keys():
                if window[key] > count:
                    most_freq = key
                    count = window[key]
            
            strikes = 0
            for key in window.keys():
                if key != most_freq:
                    strikes += window[key]
                if strikes > k:
                    return True
            return False

        
        # Optimal 
        # sliding window
        res = 0
        l, r = 0, 0
        window = {}
        while r < len(s):
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1
            r+=1
            while exceeding_window(window):
                window[s[l]] -= 1
                l += 1
            res = max(res, r-l)
            
        
        return res