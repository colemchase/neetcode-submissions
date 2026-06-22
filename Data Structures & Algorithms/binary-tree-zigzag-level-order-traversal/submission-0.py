# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def zigzag(curr, level):
            if curr:
                if level == len(res):
                    res.append([])
                res[level].append(curr.val)
                zigzag(curr.left, level+1)
                zigzag(curr.right, level+1)

        zigzag(root, 0)

        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        
        return res