# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def dive(curr):
            if curr:
                
                left = dive(curr.left)
                right = dive(curr.right)

                diff = abs(target-curr.val)

                ldiff = abs(left - target)
                rdiff = abs(right - target)
                res = [(ldiff, left), (rdiff, right), (diff, curr.val)]
                
                res.sort(key=lambda x: (x[0], x[1]))

                return res[0][1]
            return float('inf')

        return dive(root)