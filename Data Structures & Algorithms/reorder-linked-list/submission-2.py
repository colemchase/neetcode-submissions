# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find middle
        slow = head
        fast = head.next if head else head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # plus one

        # reverse right side
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge first into second
        first = head
        second = prev
        while second:
            temp_first = first.next
            temp_second = second.next

            first.next = second
            second.next = temp_first
            first = temp_first
            second = temp_second
        
    