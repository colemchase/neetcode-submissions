# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        res = ListNode(0, head)
        prev = res
        curr = head
        n = length - n + 1
        while n > 0:
            if n == 1:
                prev.next = curr.next
            else:
                temp = curr
                prev = curr
                curr = temp.next
            n -= 1
        
        return res.next