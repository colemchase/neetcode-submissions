# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        # if curr subtree size left is > k, try the right, if still too small, return 

        def getSize(node):
            if node:
                return getSize(node.left) + getSize(node.right) + 1
            return 0
        
        def findK(curr, carry):
            
            if curr:
                left = getSize(curr.left)
                right = getSize(curr.right)
                print(curr.val, left, right)
                if left + carry >= k:
                    return findK(curr.left, carry)
                if left + carry + 1 == k:
                    return curr.val
                return findK(curr.right, left + carry + 1)
                
        
        return findK(root, 0)
