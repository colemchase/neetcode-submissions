class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [0] * (n+1)
        stairs[0] = 1
        stairs[1] = 2
        if n < 3:
            return stairs[n-1]

        i = 2 
        while i < n:
            stairs[i] = stairs[i-1] + stairs[i-2]
            if i == n-1:
                return stairs[i]
            i+=1
        