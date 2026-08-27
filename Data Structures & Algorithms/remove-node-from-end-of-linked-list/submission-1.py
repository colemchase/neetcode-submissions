# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        curr = res.next

        length = 0
        # count length on list
        while curr:
            length += 1
            curr = curr.next
        
        curr = res
        n = length - n
        while n >= 0 and curr:
            if not n:
                curr.next = None if not curr.next else curr.next.next
            curr = curr.next
            n -= 1
        
        return res.next
