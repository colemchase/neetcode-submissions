class Deque:
    
    def __init__(self):
        self.q = []


    def isEmpty(self) -> bool:
        return len(self.q) == 0
        

    def append(self, value: int) -> None:
        self.q.append(value)

    def appendleft(self, value: int) -> None:
        self.q.insert(0, value)

    def pop(self) -> int:
        return self.q.pop() if not self.isEmpty() else -1

    def popleft(self) -> int:
        return self.q.pop(0) if not self.isEmpty() else -1
