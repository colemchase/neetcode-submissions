"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def postOrder(curr):
            if not curr or curr is p or curr is q:
                return curr

            left = postOrder(curr.left)
            right = postOrder(curr.right)

            if left and right:
                return curr
            
            return left if left else right

        return postOrder(root)