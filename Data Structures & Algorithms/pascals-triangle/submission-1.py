class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        while numRows > 2:
            curr = [1]
            for i in range(1, len(res[-1])):
                curr.append(res[-1][i] + res[-1][i-1])
            curr.append(1)
            res.append(curr)
            numRows -= 1
        return res