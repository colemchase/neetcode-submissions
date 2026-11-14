class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        

        def valid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[r])
        
        def isWater(r, c):
            return valid(r, c) and grid[r][c] == 0
        
        def isLand(r, c):
            return valid(r, c) and grid[r][c] == 1

        uids = {}
        counter = 2

        # find size of island
        def sizer(r, c, uid):
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if isLand(x, y):
                    if uid not in uids:
                        uids[uid] = 0
                    uids[uid] += 1
                    grid[x][y] = uid
                    stack.append((x+1, y))
                    stack.append((x-1, y))
                    stack.append((x, y+1))
                    stack.append((x, y-1))
                        

        # marking size of islands for the points of that island
        # ?? should we worry if island is marked as size 1 ??
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if isLand(r, c):
                    sizer(r, c, counter)
                    counter += 1

        # find point with most impact (sum neighbor islands size)
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if isWater(r, c):
                    curr = 1
                    seen = set()
                    for x, y in [(-1+r, 0+c), (1+r, 0+c), (0+r, -1+c), (0+r, 1+c)]:
                        if valid(x, y) and grid[x][y] > 0:
                            uid = grid[x][y]
                            if uid not in seen:
                                curr += uids[uid]
                                seen.add(uid)
                    res = max(res, curr)

        return res if res else max(uids.values())
        

