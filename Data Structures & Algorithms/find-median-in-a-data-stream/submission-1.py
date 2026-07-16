class MedianFinder:

    def __init__(self):

        self.maxheap = [] # left side
        heapq.heapify(self.maxheap)

        self.minheap = [] # right side
        heapq.heapify(self.minheap)

    def balance(self) -> None:
        while abs(len(self.maxheap) - len(self.minheap)) > 1:
            if len(self.maxheap) > len(self.minheap):
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
            else:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        

    def addNum(self, num: int) -> None:
        if len(self.maxheap) and num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -float(num))
        else:
            heapq.heappush(self.minheap, float(num))
        self.balance()

    def findMedian(self) -> float:
        if len(self.maxheap) == 0: # missing left
            return self.minheap[0]

        if len(self.minheap) == 0: # missing right
            return -self.maxheap[0]
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0: # even, pick both
            return ((self.minheap[0] - (-self.maxheap[0])) / 2) + -self.maxheap[0]

        return -self.maxheap[0] if len(self.maxheap) > len(self.minheap) else self.minheap[0]