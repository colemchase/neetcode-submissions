class Solution:
    def reorganizeString(self, s: str) -> str:
        # make a count into a max heap
        cnt = Counter(s)
        maxheap = []
        heapq.heapify(maxheap)
        for k in cnt.keys():
            heapq.heappush(maxheap, (-cnt[k], k))

        res = ""

        # start res to avoid edge cases
        res += maxheap[0][1]
        first = heapq.heappop(maxheap)
        first = (first[0]+1, first[1])
        if first[0] != 0:
            heapq.heappush(maxheap, first)

        # use max heap to find curr letter
        # move through max heap till last c in res is not curr on max heap
        while len(maxheap) > 0:
            curr = heapq.heappop(maxheap)
            if res[-1] == curr[1]: # cannot use curr, try next
                if len(maxheap) > 0:
                    temp = heapq.heappop(maxheap)
                    heapq.heappush(maxheap, curr)
                    temp = (temp[0]+1, temp[1])
                    res += temp[1]
                    if temp[0] != 0:
                        heapq.heappush(maxheap, temp)
                else:
                    return "" # cannot place another letter, no other letters to try
            else:
                res += curr[1]
                curr = (curr[0]+1, curr[1])
                if curr[0] != 0:
                    heapq.heappush(maxheap, curr)
        
        return res
                
                
