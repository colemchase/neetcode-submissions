class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        res = set(i for i in range(1, n+1))

        for relationship in trust:
            x = relationship[0]
            y = relationship[1]
            if x in res:
                res.remove(x)

        if len(res) != 1:
            return -1

        judge = list(res)[0]
        # if one person left, make sure eveyone trusts them
        p_not_trust_j = set(i for i in range(1, n+1))

        for relationship in trust:
            x = relationship[0]
            y = relationship[1]
            if y == judge:
                if x in p_not_trust_j:
                    p_not_trust_j.remove(x)



        return judge if len(p_not_trust_j) == 1 else -1