# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        # pointer to head
        pointer = ListNode(None, head)
        # have a curr node starting at head
        curr = head
        # while loop while curr 
        while curr:
            i = m
            while i > 1 and curr:
                curr = curr.next
                i-=1
            
            temp = curr
            j = n
            while j >= 0 and curr:
                curr = curr.next
                j-=1
                temp.next = curr
       

        return pointer.next