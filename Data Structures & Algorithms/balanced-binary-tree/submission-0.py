# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def dive(curr, dept):
            nonlocal res
            if curr:
                left = dive(curr.left, dept+1)
                right = dive(curr.right, dept+1)
                if abs(left - right) > 1:
                    res = False
                return max(left, right)
            return dept
        
        dive(root, 0)

        return res
        

