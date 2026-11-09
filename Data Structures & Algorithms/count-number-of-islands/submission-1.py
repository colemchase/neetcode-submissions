class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def valid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1"

        def sink(r, c):
            if valid(r, c):
                grid[r][c] = "0"
                sink(r+1, c)
                sink(r-1, c)
                sink(r, c+1)
                sink(r, c-1)

        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if valid(r, c):
                    sink(r, c)
                    res +=1
        
        return res