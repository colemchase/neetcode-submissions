class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brutal
        # Try all the permutations 
        # o n^2
        # res = 0
        # for l in range(len(prices)):
        #     for r in range(l+1, len(prices)):
        #         res = max(res, prices[r] - prices[l])
        
        # return res

        # Optimal
        # o n
        # Two pointer technique
        l = 0
        r = 0
        res = 0

        while r < len(prices):
            res = max(res, prices[r]-prices[l])
            # incr l??
            # prices[r] < prices[l]
            if prices[r] < prices[l]:
                l = r
            r+=1

        return res


