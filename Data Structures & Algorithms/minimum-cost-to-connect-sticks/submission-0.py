class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            curr = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += curr
            heapq.heappush(sticks, curr)

        return res