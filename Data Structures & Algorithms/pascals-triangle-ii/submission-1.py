class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1], [1, 1]]
        for i in range(1, rowIndex):
            curr = [1]
            for j in range(1, len(rows[-1])):
                curr.append(rows[i][j] + rows[i][j-1])
            curr.append(1)
            rows.append(curr)
        return rows[rowIndex]