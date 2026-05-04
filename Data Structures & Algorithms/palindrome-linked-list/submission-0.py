# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # send fast to the end at double speed and slow should be half as far
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse fast until slow
        

        prev = None
        while slow: # reverse second half
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
    
        return True
        