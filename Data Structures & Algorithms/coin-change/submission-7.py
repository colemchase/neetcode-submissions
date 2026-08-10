import sys
sys.setrecursionlimit(20000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        memo[0] = 0
        def dive(change):
            
            if change in memo:
                return memo[change]
            
            temp = float('inf')
            for coin in coins:
                curr = change - coin
                if curr >= 0:
                    temp = min(temp, dive(curr) + 1)
            memo[change] = temp
            return memo[change]
                    

        dive(amount)

        return memo[amount] if memo[amount] != float('inf') else -1