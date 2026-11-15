class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # max heap
        counter = Counter(s)
        heap = []
        heapq.heapify(heap)
        for key in counter.keys():
            heapq.heappush(heap, (-counter[key], key))
        
        res = ""

        # bootstrap the res
        count, c = heapq.heappop(heap)
        res += c
        if count != -1:
            heapq.heappush(heap, (count+1, c))
        
        # grab next biggest and add, if not equal to end res
        while heap:
            print(res, heap)
            addBack = []
            if heap[0][1] == res[-1]:
                count, c = heapq.heappop(heap)
                addBack.append((count, c))
            
            if not heap:
                return ""
            
            count, c = heapq.heappop(heap)
            res += c
            if count != -1:
                heapq.heappush(heap, (count+1, c))
            
            for x in addBack:
                heapq.heappush(heap, (x[0], x[1]))
        
        return res
            



        
        
                
                
