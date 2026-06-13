# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        prev = None
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        x = head # 2 4 6
        y = prev # 10 8
        
        while y:
            temp_x = x.next # save 4
            temp_y = y.next # save 8
            y.next = None # remove pointer from 10 to 8
            x.next = y # insert 10 behind 2
            y = temp_y # bump y to 8
            x = x.next # bump x to 10
            x.next = temp_x # insert 4 behind 10
            x = x.next # bumpt x to 4
       
        

        
