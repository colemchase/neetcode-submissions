class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.arr = [0] * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        self.size += 1
        if self.size > self.capacity:
            self.resize()
            print(self.size, self.capacity)
        self.arr[self.size-1] = n

    def popback(self) -> int:
        self.size-=1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        temp = [0] * self.capacity
        for i, item in enumerate(self.arr):
            temp[i] = item
        self.arr = temp

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
