class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        dj = [(0, 0, 0)]
        heapq.heapify(dj)

        dp = [[float('inf') for _ in range(len(heights[0]))] for _ in range(len(heights))]

        dp[0][0] = 0

        def valid(r, c):
            return 0 <= r < len(heights) and 0 <= c < len(heights[0])

        def calculate(r, c, x, y):
            return abs(heights[r][c]-heights[r+x][c+y])
            
        while dj:
            effort, r, c = heapq.heappop(dj)

            if r == len(heights)-1 and c == len(heights[0])-1: # base case, end cell
                return effort
            
            
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if valid(r+x, c+y):
                    new_effort = max(effort, calculate(r, c, x, y))
                    if new_effort < dp[r+x][c+y]:
                        dp[r+x][c+y] = new_effort
                        heapq.heappush(dj, (new_effort, r+x, c+y))
            

