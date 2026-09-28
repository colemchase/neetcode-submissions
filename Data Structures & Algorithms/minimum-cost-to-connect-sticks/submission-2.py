class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        heapq.heapify(sticks)
        if len(sticks) == 1:
            return 0

        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            heapq.heappush(sticks, x+y)
            res += x+y

        return res