# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        # dive, then check if leaf and self delete  
        def dive(curr):
            if curr:
                dive(curr.left)
                dive(curr.right)
                if curr.left and curr.left.val == target and not curr.left.left and not curr.left.right:
                    curr.left = None
                if curr.right and curr.right.val == target and not curr.right.left and not curr.right.right:
                    curr.right = None
                
        
        dive(root)
        if root.val == target and not root.left and not root.right:
            return None
        return root