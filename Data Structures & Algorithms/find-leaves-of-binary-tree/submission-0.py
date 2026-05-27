# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res =  []

        def deleteLeaf(curr):
            temp =  []
            if curr:
                flag = True
                if curr.left:
                    if not curr.left.left and not curr.left.right: # left is a child
                        temp.append(curr.left.val)
                        curr.left = None
                    else:
                        temp += deleteLeaf(curr.left) # left is not a child
                if curr.right:
                    if not curr.right.left and not curr.right.right: # right is a child
                        temp.append(curr.right.val)
                        curr.right = None
                    else:
                        temp += deleteLeaf(curr.right) # right is not a child
                
            return temp
        while root and (root.left or root.right):
            res.append(deleteLeaf(root))
        res.append([root.val])
        return res