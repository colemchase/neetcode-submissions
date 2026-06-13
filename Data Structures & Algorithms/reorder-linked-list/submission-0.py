# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def get_length(curr):
            if curr:
                return get_length(curr.next) + 1
            return 0
        
        length = get_length(head)
        
        if length <= 2: # no need to do the reorder
            return 
        
        # this returns end and sets node before ends next to None, making it the new end
        def grab_end(curr, prev):
            if curr and not curr.next:
                prev.next = None
                return curr
            return grab_end(curr.next, curr)
        
        
        # inserts into correct dept
        def dive(end_node, curr, curr_dept, final_dept):
            # insert the old end into the correct dept
            if curr_dept + 1 == final_dept:
                temp = curr.next
                curr.next = end_node
                end_node.next = temp
                return
            return dive(end_node, curr.next, curr_dept+1, final_dept)

        dummy = ListNode(-1, head)
        start = (length - 1) // 2
        count = start
        while count > 0:
            end_node = grab_end(dummy.next, dummy)
            final_dept = (start-count) * 2 + 1
            dive(end_node, dummy.next, 0, final_dept)
            count-=1
