import heapq

class Leaderboard:

    def __init__(self):
        self.hm = {}
        


    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.hm:
            self.hm[playerId] = 0
        self.hm[playerId] += score


    def top(self, K: int) -> int:   
        mxhp = []
        for key in self.hm.keys():
            heapq.heappush(mxhp, self.hm[key] * -1)
        
        res = 0
        for _ in range(K):
            res+= heapq.heappop(mxhp) * -1
        return res

        

    def reset(self, playerId: int) -> None:
        self.hm[playerId] = 0



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
