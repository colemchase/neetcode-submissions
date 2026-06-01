# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}

        def dive(curr, level):
            if curr:
                if level not in levels:
                    levels[level] = []
                levels[level].append(curr.val)
                dive(curr.left, level + 1)
                dive(curr.right, level +  1)
            
        dive(root, 0)
        res = []
        keys = list(levels.keys())
        keys.sort
        for key in keys:
            res.append(levels[key])

        return res