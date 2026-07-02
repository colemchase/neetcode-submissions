class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visit = [[0 for _ in range(len(grid[x]))] for x in range(len(grid))]
        
        def inBounds(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])


        def sink(x, y, v):
            if inBounds(x, y):
                if grid[x][y] == 1 and v[x][y] == 0:
                    v[x][y] = 1
                    return 1 + sink(x, y-1, v) + sink(x, y+1, v) + sink(x-1, y, v) + sink(x+1, y, v)
            return 0

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                res = max(res, sink(x, y, visit))

        return res
