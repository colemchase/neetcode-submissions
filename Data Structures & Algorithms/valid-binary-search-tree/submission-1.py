# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(curr, left, right):
            if curr:
                if not (left < curr.val < right):
                    return False
                if curr.left and curr.left.val >= curr.val: 
                    return False
                if curr.right and curr.right.val <= curr.val:
                    return False
                return validate(curr.left, left, curr.val) and validate(curr.right, curr.val, right) 
            return True
        
        return validate(root, float("-inf"), float("inf"))