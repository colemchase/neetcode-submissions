import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [g*-1 for g in gifts]
        heapq.heapify(gifts)
        
        for _ in range(k):
            gift = -heapq.heappop(gifts)
            heapq.heappush(gifts, int(-(gift ** (1/2))))

        return -sum(gifts)