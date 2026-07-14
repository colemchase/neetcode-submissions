class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))

        print(trips)

        car = 0
        minheap = []  # (e, p)
        heapq.heapify(minheap)

        for trip in trips:
            curr_p = trip[0]
            curr_s = trip[1]
            curr_e = trip[2]
            
            while len(minheap) > 0 and minheap[0][0] <= curr_s: # descrement people who got off before curr trip starts
                car -= heapq.heappop(minheap)[1]

            if car + curr_p > capacity:
                return False
            car += curr_p
            heapq.heappush(minheap, (curr_e, curr_p))

        return True