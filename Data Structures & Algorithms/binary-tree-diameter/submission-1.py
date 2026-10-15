# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dive(curr):
            if curr:
                return max(dive(curr.left), dive(curr.right)) + 1
            return 0

        if root:
            l = dive(root.left)
            r = dive(root.right)
            return max(l + r, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
            
        return 0
