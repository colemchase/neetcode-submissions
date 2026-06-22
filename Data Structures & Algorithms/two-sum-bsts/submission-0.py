# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        compliment = set()

        def buildCompliment(curr):
            if curr:
                compliment.add(target - curr.val)
                buildCompliment(curr.left)
                buildCompliment(curr.right)

        buildCompliment(root1)

        def dive(curr):
            if curr:
                if curr.val in compliment:
                    return True
                if dive(curr.left):
                    return True
                if dive(curr.right):
                    return True
            return False

        return dive(root2)