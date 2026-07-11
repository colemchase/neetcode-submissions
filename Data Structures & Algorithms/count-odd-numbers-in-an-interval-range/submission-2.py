class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        diff = (high-low+1) // 2
        if (high-low+1) % 2 and low % 2:
            return diff + 1
        return diff