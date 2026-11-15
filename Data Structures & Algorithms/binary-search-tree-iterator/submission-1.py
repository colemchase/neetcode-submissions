# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.v = []
        def inorder(curr):
            if curr:
                inorder(curr.left)
                self.v.append(curr.val)
                inorder(curr.right)
        inorder(root)
        self.i = 0

    def next(self) -> int:
        self.i+=1
        return self.v[self.i-1]


    def hasNext(self) -> bool:
        return self.i < len(self.v)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()