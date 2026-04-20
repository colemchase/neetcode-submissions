class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows
        for r in board:
            curr = set()
            for item in r:
                if item != ".":
                    if item in curr:
                        return False
                    curr.add(item)

        # cols
        for c in range(len(board)):
            curr = set()
            for r in range(len(board)):
                item = board[r][c]
                if item != ".":
                    if item in curr:
                        return False
                    curr.add(item)

        # squares
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                curr = set()
                for i in range(3):
                    for j in range(3):
                        item = board[r+i][c+j]
                        if item != ".":
                            if item in curr:
                                return False
                            curr.add(item)
        
        return True