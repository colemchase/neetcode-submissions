"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        res = []
        hm = {}
        hm[node] = Node(node.val)
        bfs = [node]

        while bfs:
            curr = bfs.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in hm:
                    hm[neighbor] = Node(neighbor.val)
                    bfs.append(neighbor)
                hm[curr].neighbors.append(hm[neighbor])
        return hm[node]
                