class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = 0
        for c in s:
            if c == "1":
                cnt+=1
        
        beg = "1" * (cnt-1) if cnt > 1 else ""
        mid = "0" * (len(s) - cnt)

        return beg + mid + "1"