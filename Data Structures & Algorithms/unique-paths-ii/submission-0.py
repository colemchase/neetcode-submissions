class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        grid = [[1 if obstacleGrid[j][i] == 0 else 0 for i in range(n)] for j in range(m)]

        i = 0
        clear = True
        while i < m:
            if grid[i][0] == 0 or not clear:
                clear = False
                grid[i][0] = 0
            i+=1
        
        i = 0
        clear = True
        while i < n:
            if grid[0][i] == 0:
                clear = False
            if not clear:
                grid[0][i] = 0
            i+=1
        

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] != 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]