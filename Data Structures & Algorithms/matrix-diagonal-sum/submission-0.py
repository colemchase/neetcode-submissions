class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0

        for i in range(len(mat)):
            res += mat[i][i]

        if len(mat) % 2 == 1:
            mid = len(mat) // 2
            res -= mat[mid][mid] 

        c = 0
        for r in range(len(mat)-1, -1, -1):
            res += mat[r][c]
            c+=1
        
        return res