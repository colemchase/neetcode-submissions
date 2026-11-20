class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # detect a cycle with union find
        # if the edge is already in the union, then return that edge
        parent = [i for i in range(len(edges)+1)]
        size = [1 for _ in range(len(edges)+1)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return

            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA

            parent[rootB] = parent[rootA]
            size[rootA] += size[rootB]

        
        for edge in edges:
            a = edge[0]
            b = edge[1]
            if find(a) == find(b):
                return edge
            union(a, b)
        
