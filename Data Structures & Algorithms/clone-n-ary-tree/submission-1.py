"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:

        
    def cloneTree(self, root: 'Node') -> 'Node':

        def dive(curr, clone):

            for i in range(len(curr.children)):
                clone.children.append(Node(curr.children[i].val, []))
                dive(curr.children[i], clone.children[i])
            return clone

        cloneT = dive(root, Node(root.val)) if root else root

        return cloneT