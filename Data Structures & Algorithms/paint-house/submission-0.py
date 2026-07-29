class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        

        dp = [0, 0, 0]

        for house in costs:
            dp0 = min(house[0] + dp[1], house[0] + dp[2])
            dp1 = min(house[1] + dp[0], house[1] + dp[2])
            dp2 = min(house[2] + dp[0], house[2] + dp[1])
            dp = [dp0, dp1, dp2]
            
        return min(dp)
