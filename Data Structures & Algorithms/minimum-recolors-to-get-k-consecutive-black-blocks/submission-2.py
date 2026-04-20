class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        res = 0
        for c in blocks[:k]:
            if c == "W":
                res+=1
        
        curr = res
        r = k
        for i in range(1, len(blocks)-k):
            if blocks[i-1] == "W":
                curr-=1
            if blocks[r] == "W":
                curr+=1
            r+=1
            res = min(curr, res)

        return res

