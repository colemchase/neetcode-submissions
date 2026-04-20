class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mn = min(self.stack[-1][1], val) if len(self.stack) > 0 else val
        self.stack.append((val, mn))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
