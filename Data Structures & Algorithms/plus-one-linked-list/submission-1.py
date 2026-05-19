# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        # go to end, return if carry
        # if carry, add to curr and return carry

        def dive(curr):
            if curr:
                curr.val += dive(curr.next)
                carry = curr.val // 10
                curr.val %= 10
                return carry
            return 1

        dummy = ListNode(0, head)
        dive(dummy)
        return dummy if dummy.val else dummy.next