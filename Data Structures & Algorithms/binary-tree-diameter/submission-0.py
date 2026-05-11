# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        # find dept of left and dept of right 
        # return the higher of the two for previous node to incorportae
        def dive(curr):
            nonlocal res
            if curr:
                left = dive(curr.left)
                right = dive(curr.right)
                res = max(res, left+right)

                return max(left, right)+1
            return 0

        dive(root)


        return res