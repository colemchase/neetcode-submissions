class Solution:
    def reverse(self, x: int) -> int:

        neg = x < 0
        y = str(-2**31) if neg else str(((2**30) - 1) + (2**30))
        buffer = 1 if neg else 0

        x = "-" + str(x)[1:][::-1] if neg else str(x)[::-1]

        if len(x) > len(y):
            return 0
        if len(x) < len(y):
            return int(x)

        for i in range(buffer, len(x)):
            if x[i] < y[i]:
                return int(x)
            if x[i] > y[i]:
                return 0

        return int(x)