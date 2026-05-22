# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hm = {}
        def dive(curr, x, y):
            if curr:
                
                if x not in hm:
                    hm[x] = []
                hm[x].append((y, curr.val))
                dive(curr.left, x-1, y+1)
                dive(curr.right, x+1, y+1)
                
        
        dive(root, 0, 0)
        
        res = []
        
        for k in list(sorted(hm.keys())):
            res.append(hm[k])
        
        for i in range(len(res)):
            res[i].sort(key = lambda x: x[0])
            col = []
            for j in range(len(res[i])):
                res[i][j] = res[i][j][1]
        
        return res