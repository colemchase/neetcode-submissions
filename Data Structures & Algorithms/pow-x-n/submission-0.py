class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x:
            return 0
        if not n:
            return 1
        res = x
        while n > 1:
            res *= x
            n -= 1
        while n < 1:
            res /= x
            n+=1
        return res