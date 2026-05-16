# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def recurse(curr, other, carry):

            if not curr and not other and not carry:
                return None
            
            if not curr:
                curr = ListNode(0, None)
            if not other:
                other = ListNode(0, None)
            
            curr.val += other.val + carry
            carry = curr.val // 10
            curr.val %= 10

            curr.next = recurse(curr.next, other.next, carry)

            return curr
        
        return recurse(l1, l2, 0)
    
    
