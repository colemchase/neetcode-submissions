class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        atl = set()
        pac = set()
        rows = len(heights)
        cols = len(heights[0])

        def inbounds(r, c):
            return 0 <= r < rows and 0 <= c < cols


        def rev(r, c, prev, ocean):
            if (r, c) not in ocean:
                if inbounds(r, c):
                    if heights[r][c] >= prev:
                        ocean.add((r, c))
                        rev(r+1, c, heights[r][c], ocean)
                        rev(r-1, c, heights[r][c], ocean)
                        rev(r, c+1, heights[r][c], ocean)
                        rev(r, c-1, heights[r][c], ocean)


        # init on edges
        for r in range(rows): # left and right
            rev(r, 0, heights[r][0], pac)
            rev(r, cols-1, heights[r][cols-1], atl)
        for c in range(cols): # top and bottom
            rev(0, c, heights[0][c], pac)
            rev(rows-1, c, heights[rows-1][c], atl)
        
        res = []

        pac = pac & atl

        for r, c in pac:
            res.append([r, c])

        return res