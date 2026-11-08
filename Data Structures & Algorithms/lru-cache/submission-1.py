class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:    

    def __init__(self, capacity: int):
        self.hm = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def update(self, key, val):

        if key in self.hm:
            drop = self.hm[key]
            drop.prev.next = drop.next
            drop.next.prev = drop.prev
            del self.hm[key]

        curr = Node(key, val)
        prev = self.tail.prev 
        prev.next = curr
        curr.prev = prev
        self.tail.prev = curr
        curr.next = self.tail
        self.hm[key] = curr

        return self.hm[key].val

    def get(self, key: int) -> int:
        if key in self.hm:
            return self.update(key, self.hm[key].val)
        return  -1

    def put(self, key: int, value: int) -> None:
        
        self.update(key, value)
        
        if len(self.hm.keys()) > self.capacity:
            drop = self.head.next
            self.head.next = drop.next
            drop.next.prev = self.head
            del self.hm[drop.key]

