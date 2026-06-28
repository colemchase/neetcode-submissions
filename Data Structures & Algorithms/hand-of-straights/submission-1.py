import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)

        res = 0
        
        while len(counter.keys()) >= groupSize:
            k = list(counter.keys())
            heapq.heapify(k)

            beg = heapq.heappop(k)
            counter[beg] -= 1
            if counter[beg] == 0:
                del counter[beg]
            
            for i in range(1, groupSize):
                if beg + i not in counter:
                    return False
                counter[beg+i] -= 1
                if counter[beg+i] == 0:
                    del counter[beg+i]
        
        return len(list(counter.keys())) == 0