# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        h = ListNode(None, head)
        prev = h
        curr = prev.next
        while curr:
            if curr.val == val: # skip this node
                if not curr.next: 
                    prev.next = None
                    break # end of list
                curr = curr.next
                prev.next = curr
                pre = prev.next
            else:
                prev = curr
                curr = curr.next
                
            
        return h.next