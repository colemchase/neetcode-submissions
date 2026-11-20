class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # weird mapping
        # [d, s]

        # topological sort

        # map all the edges using a hm     s - > [d1, d2, d3, ...]
        if not prerequisites:
            return True
        
        in_degrees = [0] * (numCourses)
        edges = {}
        for i in range(numCourses):
            edges[i] = []
        for edge in prerequisites:
            s = edge[1]
            d = edge[0]
            edges[s].append(d)
            in_degrees[d] += 1
        
        zeros = []
        for i in range(len(in_degrees)):
                if in_degrees[i] == 0 and i in edges:
                    zeros.append(i)

        res = 0
        while zeros:
            s = zeros.pop()
            res += 1
            for d in edges[s]:
                in_degrees[d] -= 1
                if in_degrees[d] == 0:
                    zeros.append(d)

        return res == numCourses