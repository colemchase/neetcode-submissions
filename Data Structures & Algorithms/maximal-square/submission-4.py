class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                matrix[r][c] = int(matrix[r][c]) 
        
        res = 0
        for r in range(len(matrix)):
            res = max(res, matrix[r][0])
        for c in range(len(matrix[0])):
            res = max(res, matrix[0][c])

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 1:
                    neighbors = min([matrix[r-1][c], matrix[r-1][c-1], matrix[r][c-1]])
                    matrix[r][c] = neighbors + 1
                    res = max(res, 1)
                res = max(res, matrix[r][c] * matrix[r][c])

        return res
