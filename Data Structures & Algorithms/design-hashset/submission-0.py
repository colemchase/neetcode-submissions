class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.arr.append(key)

    def remove(self, key: int) -> None:
        index = 0
        while index < len(self.arr):
            if self.arr[index] == key: 
                self.arr.pop(index)
                break
            index+=1
        

    def contains(self, key: int) -> bool:
        return key in self.arr


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)