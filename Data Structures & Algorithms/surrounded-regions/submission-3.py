class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # loop around the edges
        # if we find a open spot, sink it

        def inbounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        seen = set()
        def sink(r, c):
            if inbounds(r, c) and (r, c) not in seen:
                seen.add((r, c))
                if board[r][c] == "O":
                    for x, y in dirs:
                        sink(r+x, c+y)


        for r in range(rows): # left and right side of board
            sink(r, 0)
            sink(r, cols-1)
        
        for c in range(cols): # top and bottom
            sink(0, c)
            sink(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in seen:
                    board[r][c] = "X"
            