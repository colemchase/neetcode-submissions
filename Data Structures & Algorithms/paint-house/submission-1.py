class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = [0, 0, 0]

        for i in range(len(costs)):
            r = min(costs[i][0] + dp[1], costs[i][0] + dp[2])
            g = min(costs[i][1] + dp[0], costs[i][1] + dp[2])
            b = min(costs[i][2] + dp[0], costs[i][2] + dp[1])
            dp = [r, g, b]

        return min(dp)