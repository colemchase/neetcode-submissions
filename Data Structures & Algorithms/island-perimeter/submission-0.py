class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def isLand(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]):
                return grid[x][y] == 1
            return False

        
        res = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]:
                    res += 0 if isLand(x+1, y) else 1
                    res += 0 if isLand(x-1, y) else 1
                    res += 0 if isLand(x, y+1) else 1
                    res += 0 if isLand(x, y-1) else 1
        
        return res
