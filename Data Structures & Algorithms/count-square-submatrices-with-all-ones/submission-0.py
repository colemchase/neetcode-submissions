class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        
        # maximum square at a point
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[r])):
                if matrix[r][c] == 1:
                    neigh = min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1])
                    matrix[r][c] = neigh + 1
        
        res = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                res += matrix[r][c]

        return res