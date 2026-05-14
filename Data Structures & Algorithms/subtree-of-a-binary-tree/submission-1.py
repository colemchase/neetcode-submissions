# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        def helper(curr, other):
            if curr and other:
                if curr.val == other.val:
                    return helper(curr.left, other.left) and helper(curr.right, other.right)
                else:
                    return False
            
            if not curr and not other:
                return True
            
            return False


        
        def dive(curr):
            if curr:
                if curr.val == subRoot.val and helper(curr, subRoot):
                    return True
                return dive(curr.left) or dive(curr.right)
            return False
        return dive(root)