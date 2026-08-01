import sys
sys.setrecursionlimit(20000)





class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dive(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1+dive(amount-coin))
            memo[amount] = res
            return res
        res = dive(amount)
        return -1 if res == float('inf') else res
