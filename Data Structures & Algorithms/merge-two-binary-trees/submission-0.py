# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dive(curr, other):
        
            if curr or other:
                if not curr:
                    curr = TreeNode(0, None, None)
                if not other:
                    other = TreeNode(0, None, None)
                curr.val += other.val
                curr.left = dive(curr.left, other.left)
                curr.right = dive(curr.right, other.right)
  
                return curr
            return None
                
        res = dive(root1, root2)

        return res