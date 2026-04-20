class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        target = (m-1, n-1)

        hm = {}

        def dive(row, col):
            if row < m and col < n:
                if (row, col) in hm:
                    return hm[(row,col)]
                curr = 1 if (row, col) == target else 0
                hm[(row, col)] = curr + dive(row+1, col) + dive(row, col+1)
                return hm[(row, col)]
            return 0
        return dive(0, 0)