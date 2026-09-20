# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        res = []
        heapq.heapify(res)
        for curr in lists:
            while curr:
                heapq.heappush(res, Node(curr.val))
                curr = curr.next
        
        head = ListNode(0)
        curr = head
        while res:
            curr.next = ListNode(heapq.heappop(res).val)
            curr = curr.next
        
        return head.next
        


