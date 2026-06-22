# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        
        def postOrderTraversal(curr):
            if not curr or curr is p or curr is q:
                return curr
            
            left = postOrderTraversal(curr.left)
            right = postOrderTraversal(curr.right)

            if left and right:
                return curr

            if left:
                return left
            if right:
                return right
            
        
        return postOrderTraversal(root)
        