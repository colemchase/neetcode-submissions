class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class MyLinkedList:
    

    def __init__(self):
        self.h = Node(-1, None)
        

    def get(self, index: int) -> int:
        curr = self.h.nxt
        while index > 0 and curr:
            index -= 1
            curr = curr.nxt
            
        return curr.val if curr else -1


    def addAtHead(self, val: int) -> None:
        temp = self.h.nxt
        self.h.nxt = Node(val, temp)

    def addAtTail(self, val: int) -> None:
        curr = self.h
        while curr.nxt:
            curr = curr.nxt
        curr.nxt = Node(val, None)


    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.h

        while index > 0:
            index -= 1
            curr = curr.nxt
        
        temp = curr.nxt
        curr.nxt = Node(val, temp)


    def deleteAtIndex(self, index: int) -> None:
        prev = self.h
        curr = self.h.nxt
        
        while index  > 0:
            index -= 1
            prev = curr
            curr = curr.nxt
        
        prev.nxt = curr.nxt if curr else None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)