class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = [[False for c in range(len(board[r]))] for r in range(len(board))]

        def inBounds(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[r]) and not visited[r][c]

        def dive(r, c, rem):
            if inBounds(r, c):
                if rem[0] == board[r][c]: # valid current spot
                    visited[r][c] = True
                    if len(rem) == 1:  # solved
                        return visited[r][c]
                    else:
                        # try to dive further
                        if dive(r+1, c, rem[1:]) or dive(r-1, c, rem[1:]) or dive(r, c+1, rem[1:]) or dive(r, c-1, rem[1:]):
                            return visited[r][c]
                        visited[r][c] = False # undo because it didnt work
                    return visited[r][c]
            return False


        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if dive(r, c, word):
                        return True
                

        return False