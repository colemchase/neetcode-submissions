class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Brutal
        # Rows, Columns, and squares
        # for each position, check all the needed positions as if never seen
        # O n ^ 2
        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr != ".":
                    for x in range(9):
                        if x != c and curr == board[r][x]:
                            return False
        
        for c in range(9):
            for r in range(9):
                curr = board[r][c]
                if curr != ".":
                    for x in range(9):
                        if x != r and curr == board[x][c]:
                            return False

        for start_c in range(0, 9, 3):
            for start_r in range(0, 9, 3):
                # starting point
                for c in range(start_c, start_c+3):
                    for r in range(start_r, start_r+3):
                        curr = board[r][c] # number we are checking does not have dups
                        if curr != ".":
                            for x in range(start_c, start_c+3):
                                for y in range(start_r, start_r+3):
                                    if c != x and r != y and curr == board[y][x]:
                                        return False

        return True