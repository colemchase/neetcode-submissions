class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brutal
        # Try all the permutations 
        res = 0
        for l in range(len(prices)):
            for r in range(l+1, len(prices)):
                res = max(res, prices[r] - prices[l])
        
        return res