class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)
        i = 0
        res = 0
        while i < len(intervals)-1: # start going through each interval
            if intervals[i][1] > intervals[i+1][0]: # next is overlapping
                if intervals[i][1] < intervals[i+1][1] : # next goes further so pop it
                    intervals.pop(i+1)
                else:
                    intervals.pop(i) # curr is further so pop it
                res += 1
                continue
            i+=1
        
        return res