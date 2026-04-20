import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [g*-1 for g in gifts]
        print(gifts)
        heapq.heapify(gifts)

        for i in range(k):
            curr = heapq.heappop(gifts)
            curr = math.isqrt(-curr)
            heapq.heappush(gifts, -curr)
        
        res = 0

        for num in gifts:
            res+=num

        return res*-1        
