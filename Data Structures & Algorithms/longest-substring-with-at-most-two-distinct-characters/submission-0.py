class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        hm = {}
        res = 0

        i = 0
        j = i + res
        while i < (len(s)) and j < len(s):
            curr = s[j]
            if curr not in hm:
                hm[curr] = 0
            hm[curr] += 1

            while len(hm.keys()) > 2:
                left = s[i]
                hm[left] -= 1
                if hm[left] == 0:
                    del hm[left]
                i += 1
            
            res = max(res, j-i+1)
            j+=1

        return res

                
                

                    
    