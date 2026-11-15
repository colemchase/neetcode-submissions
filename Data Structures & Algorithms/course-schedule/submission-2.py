class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # weird mapping direction
        # find if there is a cycle
        # topologically sorting, khans algo

        if len(prerequisites) == 0:
            return True

        # generate inDegrees[courseNumber]
        inDegrees = [0] * numCourses # not sure if n, can be determined with more code structure
        edges = {i:[] for i in range(numCourses)}
        for d, s in prerequisites:
            inDegrees[d] += 1
            edges[s].append(d)

        zeros = []
        for i in range(numCourses):
            if inDegrees[i] == 0:
                zeros.append(i)
        
        index = 0
        topo = [0] * numCourses
        while zeros:
            curr = zeros.pop()
            topo[curr] = index
            index += 1

            for d in edges[curr]:
                inDegrees[d] -= 1
                if inDegrees[d] == 0:
                    zeros.append(d)
        
        return index == numCourses
            
