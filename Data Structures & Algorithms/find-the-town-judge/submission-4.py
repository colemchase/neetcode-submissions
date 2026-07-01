class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = [(0, 0) for _ in range(1, n+1)]

        for relationship in trust:
            x = relationship[0] - 1
            y = relationship[1] - 1
            res[x] = (res[x][0], res[x][1] + 1)
            res[y] = (res[y][0] + 1, res[y][1])

        for i, person in enumerate(res):
            if person[0] == n -1 and person[1] == 0:
                return i+1
                
        return -1

        