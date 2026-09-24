import sys
sys.setrecursionlimit(20000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        memo[0] = 0
        

        def dp(memo, amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = float('inf')
            for coin in coins:
                if amount-coin >= 0:
                    res = min(1+dp(memo, amount-coin), res)
            memo[amount] = res
            return memo[amount]

        dp(memo, amount)

        return memo[amount] if memo[amount] != float('inf') else -1
                