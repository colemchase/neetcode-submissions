class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = 0
        for c in s:
            if c == "1":
                cnt+=1
        
        return ("1" * (cnt-1) if cnt > 1 else "") + "0" * (len(s) - cnt) + "1"