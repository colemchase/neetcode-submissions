# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # merge list2 into list1

        head = ListNode(None, None)
        curr = head
        if not list1 and not list2:
            return None
        
        while list1 or list2:
    
            if list1 and list2:
                if list1.val < list2.val:
                    curr.val = list1.val
                    list1 = list1.next
                else:
                    curr.val = list2.val
                    list2 = list2.next
            elif list1:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next
            curr.next = ListNode(None, None) if list1 or list2 else None
            curr = curr.next


        return head