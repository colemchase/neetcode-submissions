# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def diveUp(curr, prev, streak):
            if curr:
                if prev.val + 1 == curr.val:
                    streak += 1
                    return max(diveUp(curr.left, curr, streak), diveUp(curr.right, curr, streak))
            return streak
        
        def diveDown(curr, prev, streak):
            if curr:
                if prev.val - 1 == curr.val:
                    streak += 1
                    return max(diveDown(curr.left, curr, streak), diveDown(curr.right, curr, streak))
            return streak

        def dive(curr):
            if curr:
                left = max(diveUp(curr.left, curr, 1), diveDown(curr.left, curr, 1))
                right = max(diveUp(curr.right, curr, 1), diveDown(curr.right, curr, 1))
                total = left +  right
                total -=1
                return max(total, dive(curr.left), dive(curr.right))
            return 0
               
        return dive(root)

