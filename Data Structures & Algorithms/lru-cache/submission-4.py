class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1

        # stitch it out
        curr = self.hm[key]
        curr.prev.nxt = curr.nxt
        curr.nxt.prev = curr.prev

        # update tail
        self.tail.prev.nxt = curr
        curr.prev = self.tail.prev
        curr.nxt = self.tail
        self.tail.prev = curr

        return self.hm[key].val

    def put(self, key: int, value: int) -> None:
        curr = Node(key, value)
        if key in self.hm: # stitch it out
            curr = self.hm[key]
            curr.prev.nxt = curr.nxt
            curr.nxt.prev = curr.prev
            curr.val = value
        else:
            self.hm[key] = curr

        # add in at tail
        prev = self.tail.prev
        prev.nxt = curr
        curr.prev = prev
        curr.nxt = self.tail
        self.tail.prev = curr

        
        # check if cache needs eviction, pop back
        if self.capacity - len(self.hm.keys()) < 0 :
            del self.hm[self.head.nxt.key]
            self.head.nxt = self.head.nxt.nxt
            self.head.nxt.prev = self.head
        


        

