class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        left = toBeRemoved[0]
        right = toBeRemoved[1]

        def chop(x, y, left, right):
            if left <= x and right < y: # left if flush
                return [[right, y]]
            if right >= y and left > x: # right flush
                return [[x, left]]
            return [[x, left], [right, y]]
                

        i = 0
        while i < len(intervals):
            curr = intervals[i]
            # delete whole thing
            if left <= curr[0] and curr[1] <= right:
                intervals.pop(i)
                continue
            # not in it
            if curr[1] <= left or curr[0] >= right:
                i+=1
                continue

            # chop split, chop left, chop right
            intervals = intervals[:i] + chop(curr[0], curr[1], left, right) + intervals[i+1:]
            i+=1

        return intervals