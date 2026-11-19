class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # loop thru grid for a chest
        # only trigger distance updates on a treasure chest
            # only update if distance twice if less than current distance pos and 
        # can we just use dfs for updating distances

        def inbounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[r])
        

        bfs = []

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0: # found chest
                    bfs.append((r+1, c, 1))
                    bfs.append((r-1, c, 1))
                    bfs.append((r, c+1, 1))
                    bfs.append((r, c-1, 1))
        
        while bfs:
            r, c, dist = bfs.pop(0)
            if inbounds(r, c):
                if dist < grid[r][c]:
                    grid[r][c] = dist
                    bfs.append((r+1, c, dist+1))
                    bfs.append((r-1, c, dist+1))
                    bfs.append((r, c+1, dist+1))
                    bfs.append((r, c-1, dist+1))
    
        
