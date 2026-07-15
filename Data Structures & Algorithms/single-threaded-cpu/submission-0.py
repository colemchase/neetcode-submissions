class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i in range(len(tasks)):
            tasks[i] = (tasks[i][0], tasks[i][1], i)
        tasks.sort(key=lambda x: x[0])
        
        
        # minheap with (processing_time, index)
        minheap = []
        heapq.heapify(minheap)
        clock = 0
        res = []
        
        i = 0
        
        while i < len(tasks) or len(minheap):


            while i < len(tasks) and clock >= tasks[i][0]: # add available tasks to window
                heapq.heappush(minheap, (tasks[i][1], tasks[i][2]))
                i+=1
            
            if len(minheap) > 0: # process next item in window
                curr_p, curr_i = heapq.heappop(minheap)
                clock += curr_p
                res.append(curr_i)
            else: # nothing in window, shift window
                clock = tasks[i][0] if i < len(tasks) else clock
            

        return res
