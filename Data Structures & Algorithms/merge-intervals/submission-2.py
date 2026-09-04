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
        print(intervals)

        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
                intervals.pop(i)
            else:
                i+=1
        return intervals
