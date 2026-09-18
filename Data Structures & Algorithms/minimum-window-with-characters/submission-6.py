class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        l = r = 0
        res_length = float('inf')
        res = ""

        t_count = Counter(t)
        window = {}
        completed_keys = set()

        while r < len(s):
            right = s[r]
            if right not in window:
                window[right] = 0
            window[right] += 1
            if right in t_count and window[right] >= t_count[right]:
                completed_keys.add(right)
            r+=1
            
            while len(completed_keys) == len(t_count.keys()): # decr until window does not have t in it
                if r-l < res_length:
                    res_length = r-l
                    res = s[l:r]

                left = s[l]
                window[left] -= 1
                if window[left] < t_count[left] and left in completed_keys:
                    completed_keys.remove(left)
                l+=1

        return res