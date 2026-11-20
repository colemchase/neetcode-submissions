class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indeg = [0] * numCourses
        edges = {}
        for i in range(numCourses):
            edges[i] = []

        for edge in prerequisites:
            d = edge[0]
            s = edge[1]
            edges[s].append(d)
            indeg[d] += 1
        
        zeros = []
        for i in range(len(indeg)):
            if indeg[i] == 0:
                zeros.append(i)

        res = []
        while zeros:
            curr = zeros.pop()
            res.append(curr)
            for d in edges[curr]:
                indeg[d] -= 1
                if indeg[d] == 0:
                    zeros.append(d)
        
        return res if len(res) == numCourses else []
            
            
        
