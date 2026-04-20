class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.b = [[0 for _ in range(n)] for _ in range(n)]

    def score(self) -> int:
        # horizontal
        for row in self.b:
            curr = list(set(row))
            if len(curr) == 1 and curr[0] != 0:
                return curr[0]
        
        # vertical
        for col in range(self.n):
            curr = set()
            for row in range(self.n):
                curr.add(self.b[row][col])
            curr = list(curr)
            if len(curr) == 1 and curr[0] != 0:
                return curr[0]
        
        # diag neg
        curr = set()
        for i in range(self.n):
            curr.add(self.b[i][i])
        curr = list(curr)
        if len(curr) == 1 and curr[0] != 0:
                return curr[0]
        
        # diag pos 
        curr = set()
        i = self.n - 1
        j = 0
        while i >= 0:
            curr.add(self.b[i][j])
            i-=1
            j+=1
        curr = list(curr)
        if len(curr) == 1 and curr[0] != 0:
                return curr[0]
        
        return 0

    def move(self, row: int, col: int, player: int) -> int:
        self.b[row][col] = player
        res = self.score()
        return res


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
