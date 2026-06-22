# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        compliment = set()

        def bs(compliment, curr):
            if curr:
                if curr.val == compliment:
                    return True
                return bs(compliment, curr.left) or bs(compliment, curr.right)
            return False
                


        def dive(curr):
            if curr:
                if bs(target - curr.val, root2):
                    return True
                return dive(curr.left) or dive(curr.right)
            return False

        return dive(root1)