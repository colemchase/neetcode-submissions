# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0, l1)
        c1 = head.next
        c2 = l2
        carry = 0

        if c1.val + c2.val == 0:
            return c1

        while c1.val or c2.val or carry:

            c1.val += c2.val + carry
            carry = 0
            if c1.val > 9:
                carry = 1
                c1.val = c1.val - 10
            
            if not c1.next:
                c1.next = ListNode(0, None)
            if not c2.next:
                c2.next = ListNode(0, None)
            c1 = c1.next
            c2 = c2.next
        
        curr = head.next
        while curr:
            if curr.next and curr.next.val == 0 and not curr.next.next:
                curr.next = None
            curr = curr.next
        
        return head.next
    
    
