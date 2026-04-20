class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = [] # stack of both the letter and the number of matching adjacent prior letters
        for c in s:
            if len(res) > 0:
                if res[-1][0] == c:
                    if res[-1][1] == k - 1:
                        for _ in range(k-1):
                            res.pop()
                    else:
                        res.append((c, res[-1][1]+1))
                else:
                    res.append((c, 1))
            else:
                res.append((c, 1))
                
        res = [x[0] for x in res]
        return "".join(res)
                
