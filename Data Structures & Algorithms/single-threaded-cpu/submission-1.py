class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i] = tasks[i] + [i] 
        tasks.sort(key=lambda x: x[0])
        
        window = []
        heapq.heapify(window)
        res = []
        clock = 0
        while len(res) < len(tasks):
            clock = max(clock, tasks[len(res)][0])
            i = len(res) + len(window)
            while i < len(tasks) and clock >= tasks[i][0]:
                heapq.heappush(window, (tasks[i][1], tasks[i][2]))
                i+=1
                            
            curr = heapq.heappop(window)
            clock += curr[0]
            res.append(curr[1])

        return res