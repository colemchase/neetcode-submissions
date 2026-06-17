# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if current node has both, check if the children do too, if so, return those

        # contains
        def contains(curr, x):
            if curr:
                if curr.val == x:
                    return True
                return contains(curr.left, x) or contains(curr.right, x)
            return False

        # search
        bfs = [root]
        i = 0
        while i < len(bfs):
            curr = bfs[i]
            if curr.left:
                bfs.append(curr.left)
            if curr.right:
                bfs.append(curr.right)
            i += 1                   

        for node in bfs[::-1]:
            if contains(node, p.val) and contains(node, q.val):
                return node
        
