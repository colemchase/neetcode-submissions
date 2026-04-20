class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        groups = list(zip(position, speed))

        groups.sort(key=lambda x: x[0], reverse=True)

        res = []

        for g in groups:
            p, s = g
            res.append((target-p) / s)
            
            if len(res) > 1 and res[-2] >= res[-1]:
                res.pop()

        return len(res)