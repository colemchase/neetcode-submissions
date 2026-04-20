class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i = 0
        self.j = 0
        self.v1 = v1
        self.v2 = v2
        self.flip = False

    def next(self) -> int:
        if self.hasNext():
            if not self.flip:
                self.flip = True
                if self.i < len(self.v1):
                    res = self.v1[self.i]
                    self.i+=1
                    return res
                return self.next()
            else:
                self.flip = False
                if self.j < len(self.v2):
                    res = self.v2[self.j]
                    self.j+=1
                    return res
                return self.next()


    def hasNext(self) -> bool:
        return self.i < len(self.v1) or self.j < len(self.v2)


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
