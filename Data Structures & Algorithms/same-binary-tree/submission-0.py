# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def samesies(x, y):
            if x or y:
                if x and y and x.val == y.val:
                    return True and samesies(x.left, y.left) and samesies(x.right, y.right)
                return False
            return True
        
        return samesies(p, q)