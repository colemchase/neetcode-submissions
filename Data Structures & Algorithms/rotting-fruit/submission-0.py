class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        bfs = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    bfs.append((i, j))

        def fruit(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] == 1
        
        def spread(r, c):
            if fruit(r, c):
                grid[r][c] = 2
                return True
            return False

        res = 0

        while bfs:
            temp = []

            while bfs:
                r, c = bfs.pop()
                if spread(r-1, c):
                    temp.append((r-1, c))
                if spread(r+1, c):
                    temp.append((r+1, c))
                if spread(r, c-1):
                    temp.append((r, c-1))
                if spread(r, c+1):
                    temp.append((r, c+1))
            bfs += temp
            res += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return res-1 if res else 0
