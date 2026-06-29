class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            if -heap[0] < -heap[1]:
                heapq.heappop(heap)
            elif -heap[0] == -heap[1]:
                heapq.heappop(heap)
                heapq.heappop(heap)
            else:
                big = heapq.heappop(heap)
                smol = heapq.heappop(heap)
                heapq.heappush(heap, big - smol)
        
        return -heap[0] if len(heap) else 0

