"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:

        def dept(curr, d):
            if curr:
                temp = d
                for child in curr.children:
                    temp = max(temp, dept(child, d+1))
                return temp
            return d
        
        def dive(curr):

            if curr:
                # find dept of each child, compare to all other children for max dept
                arr = [dept(child, 1) for child in curr.children]
                arr.sort()
                
                res = arr[-1] + arr[-2] if len(arr) > 1 else arr[-1] if len(arr) == 1 else 0
                for child in curr.children:
                    res = max(res, dive(child))
                return res
            return 0

        return dive(root)

                    