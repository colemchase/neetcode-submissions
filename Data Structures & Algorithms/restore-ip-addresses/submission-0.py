class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res

        def backtrack(subset, i, j):
            if i >= len(s) or j == 4:
                if j == 4 and i == len(s):
                    res.append(subset[:-1])
                return
            
            # make a valid 1 2 or 2 digit num with no leading zeros
            for k in range(1, 4):
                if i + k > len(s):
                    break
                curr = s[i:i+k]
                
                if len(curr) > 1 and curr[0] == "0" or int(curr) > 255:
                    continue
                backtrack(subset + curr + ".", i+len(curr), j+1)
                    
        
        backtrack("", 0, 0)
        return res