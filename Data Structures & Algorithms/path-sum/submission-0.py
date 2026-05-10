# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def ps(node, curSum):
            if node:
                if node.val + curSum == targetSum and not node.left and not node.right:
                    return True
                return ps(node.left, curSum + node.val) or ps(node.right, curSum + node.val)
            return False
            
        return ps(root, 0)