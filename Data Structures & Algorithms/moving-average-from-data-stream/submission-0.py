class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.total = 0
        self.count = 0
        self.size = size

    def next(self, val: int) -> float:
        self.total+=val
        self.arr.append(val)
        if self.count < self.size:
            self.count+=1
            return self.total / self.count
        self.total -= self.arr.pop(0)
        return self.total / self.size

    


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
