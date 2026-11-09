# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def recurse(prev):
            if prev.next and prev.next.next:
                first = prev.next
                second = prev.next.next
                third = prev.next.next.next

                first.next = third
                second.next = first
                prev.next = second
                recurse(first)
        
        res = ListNode(-1, head)
        recurse(res)
        return res.next
        
