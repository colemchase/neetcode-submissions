class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(0, n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return
            
            if size[rootA] < size[rootB]:
                rootB, rootA = rootA, rootB

            parent[rootB] = rootA
            size[rootA] += size[rootB]
        
        for x, y in edges:
            union(x, y)

        for i in range(len(parent)):
            find(i)
        
        return len(set(parent))

        
