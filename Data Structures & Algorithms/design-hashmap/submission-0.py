class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        i = 0
        while i < len(self.arr):
            if self.arr[i][0] == key:
                self.arr[i][1] = value
                return
            i+=1
        self.arr.append([key,value])
        

    def contains(self, key: int) -> bool:
        i = 0
        while i < len(self.arr):
            if self.arr[i][0] == key:
                return True
            i+=1
        return False

    def get(self, key: int) -> int:
        i = 0
        print(self.arr)

        while i < len(self.arr):
            if self.arr[i][0] == key:
                return self.arr[i][1]
            i+=1
        return -1

    def remove(self, key: int) -> None:
        i = 0
        while i < len(self.arr):
            if self.arr[i][0] == key:
                self.arr.pop(i)
                break
            i+=1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)