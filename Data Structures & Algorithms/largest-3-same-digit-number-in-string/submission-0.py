class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        for i in range(1, len(num) - 1):
            if num[i] == num[i-1] and num[i] == num[i+1]:
                res = max(int(num[i-1:i+2]), res)
        
        if res == 0:
            return "000"
            
        return "" if res == -1 else str(res)