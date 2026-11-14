class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = list(range(n))
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
                rootA, rootB = rootB, rootA
            
            parent[rootB] = parent[rootA]
            size[rootA] += size[rootB]
        
        for a, b in edges:
            union(a, b)

        for i in range(n):
            find(i)
        
        return len(set(parent))

        
