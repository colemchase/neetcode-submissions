class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hm = {}
        for i, c in enumerate(keyboard):
            hm[c] = i

        res = 0
        prev = 0
        for c in word:  
            curr = hm[c]
            res += abs(curr-prev)
            prev = curr
        return res