import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        heapq.heapify(self.left)
        heapq.heapify(self.right)


    def balance(self) -> None:
        while len(self.left) - len(self.right) > 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        
        while len(self.right) - len(self.left) > 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))
        

    def addNum(self, num: int) -> None:
        if self.left and num > -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        self.balance()

    def findMedian(self) -> float:

        # uneven, return front of longest side
        if len(self.left) - len(self.right):
            if len(self.left):
                if len(self.right):
                    if len(self.left) > len(self.right):
                        return -self.left[0]
                    else: 
                        return self.right[0]
                return -self.left[0]
            return self.right[0]


        # even
        extra = (self.right[0]+self.left[0]) / 2
        base = min(-self.left[0], self.right[0])
        return extra + base
        