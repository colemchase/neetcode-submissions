class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        row = [0] * m
        col = [0] * n

        res = 0
        for i in range(m):
            for j in range(n):
                curr = picture[i][j]
                if curr == 'B':
                    row[i] += 1
                    col[j] += 1
        
        for i in range(m):
            for j in range(n):
                res += 1 if picture[i][j] == 'B' and row[i] == 1 and col[j] == 1 else 0
                    
        return res
