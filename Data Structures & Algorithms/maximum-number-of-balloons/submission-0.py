class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)

        def minChar(low, c, hm):
            if c in hm:
                md = 1
                if c == "l" or c == "o":
                    md = 2
                return min(low, hm[c]//md)
            return 0
        
        res = float('inf')
        arr = ['b', 'a', 'l', 'o', 'n']
        for item in arr:
            res = minChar(res, item, cnt)

        return res