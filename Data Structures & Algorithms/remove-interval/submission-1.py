class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        left = toBeRemoved[0]
        right = toBeRemoved[1]                

        i = 0
        while i < len(intervals):
            curr = intervals[i]
            x = curr[0]
            y = curr[1]
            # delete whole thing
            if left <= x and y <= right:
                intervals.pop(i)
                continue
            # not in it
            if y <= left or x >= right:
                i+=1
                continue

            # chop split, chop left, chop right
            res = [[x, left], [right, y]] # chop
            if left <= x and right < y: # left if flush or more
                res = [[right, y]]
            if right >= y and left > x: # right flush or more
                res = [[x, left]]
            
            intervals = intervals[:i] + res + intervals[i+1:]
            i+=1

        return intervals