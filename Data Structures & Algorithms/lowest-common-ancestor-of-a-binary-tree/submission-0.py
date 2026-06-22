# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def hasOne(curr, x):
            if curr:
                if curr.val == x.val:
                    return True
                return hasOne(curr.left, x) or hasOne(curr.right, x)
            return False


        def hasBoth(curr):
            if curr:
                if hasOne(curr, p) and hasOne(curr, q):
                    return True
            return False

        
        def postOrderTraversal(curr):
            if curr:
                left = postOrderTraversal(curr.left)
                right = postOrderTraversal(curr.right)
                if left:
                    return left
                if right:
                    return right

                if hasBoth(curr):
                    return curr
        
        return postOrderTraversal(root)
        