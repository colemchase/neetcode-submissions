class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # topological sort, khans algo ish
        # check for cycles by storing which node saw it if already seen
        if not edges: # empty graph
            return True
        if len(edges) == n: # cycle present
            return False

        graph = {}
        for i in range(n):
            graph[i] = []
        
        for edge in edges:
            a = edge[0]
            b = edge[1]

            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        dfs = [0]
        while dfs:
            curr = dfs.pop(0)
            if curr not in visited:
                visited.add(curr)
                for d in graph[curr]:
                    dfs.append(d)

        
        return len(visited) == n


