class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def valid_window(window, t_count): # beyond
            for key in t_count:

                if key not in window or t_count[key] > window[key]:
                    return False
            return True

        
        l = r = 0
        res_length = float('inf')
        res = ""
        t_count = Counter(t)
        window = {}
        while r < len(s):
            if s[r] not in window:
                window[s[r]] = 0
            window[s[r]] += 1
            r+=1

            while valid_window(window, t_count): # decr until window does not have t in it
                window[s[l]] -= 1
                l+=1
            # add left back in, check for validity to update res
            if l:
                l-=1
                window[s[l]] += 1
                if valid_window(window, t_count) and r-l < res_length:
                    res = s[l:r]
                    res_length = len(res)
                window[s[l]] -=1
                l+=1

        return res

