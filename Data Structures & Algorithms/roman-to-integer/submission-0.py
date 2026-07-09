class Solution:
    def romanToInt(self, s: str) -> int:
        stx = [0]

        hm = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        for c in s:
            if len(s) == 0 or stx[-1] >= hm[c]:
                stx.append(hm[c])
            else:
                stx[-1] = hm[c] - stx[-1]

        return sum(stx)