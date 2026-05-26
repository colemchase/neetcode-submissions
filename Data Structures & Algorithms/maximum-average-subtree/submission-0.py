# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # get total count and sub val subtrees at node

        
        # # get max average subtree

        def maxAve(curr):
            if curr:
                left_tot, left_cnt, left_max_ave = maxAve(curr.left)
                right_tot, right_cnt, right_max_ave = maxAve(curr.right)
                tot = left_tot + right_tot + curr.val
                cnt = left_cnt + right_cnt + 1
                ave = 1.0 * tot / cnt
                return (tot, cnt, max(left_max_ave, right_max_ave, ave))
            return (0, 0, 0)

        _, _ , res = maxAve(root)

        return res