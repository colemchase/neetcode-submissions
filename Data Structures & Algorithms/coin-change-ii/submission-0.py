class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = {} # change -> res


        def dfs(i, change):
            if change == 0:
                return 1
            
            if i >= len(coins) or change < 0:
                return 0

            if (i, change) in dp:
                return dp[(i, change)]
            
            skip = dfs(i+1, change)
            take = dfs(i, change-coins[i])
            dp[(i, change)] = skip + take
            
            return dp[(i, change)]
        
        return dfs(0, amount)