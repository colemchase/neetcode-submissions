# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dive(curr):
            if curr:
                return 1 + max(dive(curr.left), dive(curr.right))
            return 0
        
        return dive(root)