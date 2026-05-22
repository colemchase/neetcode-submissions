# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def dive(curr, prev, streak):
            if curr:
                if prev.val + 1 == curr.val:
                    streak += 1
                else:
                    return max(streak, dive(curr.left, curr, 1), dive(curr.right, curr, 1))
                return max(dive(curr.left, curr, streak), dive(curr.right, curr, streak))
            return streak
                    
               
        return dive(root, root, 1)