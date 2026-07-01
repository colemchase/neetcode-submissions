class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        def helper(r, c, target):
            nonlocal visit
            if 0 <= r < len(image) and 0 <= c < len(image[r]):
                if image[r][c] == target and (r, c) not in visit:
                    image[r][c] = color
                    visit.add((r, c))
                    helper(r+1, c, target)
                    helper(r-1, c, target)
                    helper(r, c+1, target)
                    helper(r, c-1, target)


        helper(sr, sc, image[sr][sc])

        return image
