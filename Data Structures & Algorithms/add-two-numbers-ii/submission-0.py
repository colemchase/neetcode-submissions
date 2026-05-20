# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def rev(node):
            curr, prev = node, None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        l2 = rev(l2)
        l1 = rev(l1)
    
        dummy = ListNode(0, None)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tail = tail.next

        return rev(dummy.next)



        