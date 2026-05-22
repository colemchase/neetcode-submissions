# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dive(curr):
            if curr:
                if low <= curr.val <= high:
                    return curr.val + dive(curr.left) + dive(curr.right)
                elif curr.val < low:
                    return dive(curr.right)
                else:
                    return dive(curr.left)
            return 0
        
        return dive(root)