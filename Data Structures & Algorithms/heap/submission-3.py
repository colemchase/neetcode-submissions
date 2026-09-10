class MinHeap:
    
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)
        print(self.heap)

    def pop(self) -> int:
        if not len(self.heap):
            return -1
        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        print(self.heap)
        return res

    def top(self) -> int:
        return self.heap[0] if len(self.heap) else -1

    
    def heapify_up(self, i):
        parent = (i-1) // 2
        if parent >= 0 and self.heap[i] < self.heap[parent]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.heapify_up(parent)

    
    def heapify_down(self, i):
        if i < len(self.heap):
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if  left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if  right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != i:
                temp = self.heap[i]
                self.heap[i] = self.heap[smallest]
                self.heap[smallest] = temp
                self.heapify_down(smallest)
        


    def heapify(self, nums: List[int]) -> None:
        self.heap = nums
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.heapify_down(i)
