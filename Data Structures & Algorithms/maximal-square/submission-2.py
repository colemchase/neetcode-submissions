class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = int(matrix[r][c]) 
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]:
                    if r != 0 and c != 0:
                        matrix[r][c] = min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1]) + 1
                    else:
                        res = max(res, matrix[r][c])
                    res = max(res, matrix[r][c]*matrix[r][c])

        return res
