class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        minheap = []
        heapq.heapify(minheap)
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                heapq.heappush(minheap, (dist, i, j))

        w = [-1 for _ in range(len(workers))]
        b = [False for _ in range(len(bikes))]
        placed = 0
        while placed < len(workers):
            dist, worker_i, bike_j = heapq.heappop(minheap)
            if w[worker_i] == -1 and not b[bike_j]:
                w[worker_i] = bike_j
                b[bike_j] = True
                placed += 1
        
        return w