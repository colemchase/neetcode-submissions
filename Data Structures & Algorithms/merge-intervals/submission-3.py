class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # merge strategy
        # comparing two intervals 
        # earlier on left, later on right
        # [1, 3]   [2, 5]
        # right start is <= left end: left end = right end
        # otherwise append right

        
        # Brutal: n^2 (bad sort, merge)
        # find earliest remainiing interval, append to other sorted array, repeat
        # merge interval


        # Optimal: n log n (sort first, then move through array linearly)
        # merge sort
        # merge interval
        intervals.sort(key=lambda x: (x[0], x[1]))
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res
