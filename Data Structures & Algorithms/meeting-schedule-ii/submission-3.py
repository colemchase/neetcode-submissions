"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: (x.start, x.end))
        i = 1
        res = [[intervals[0]]]

        for interval in intervals[1:]:
            placed = False
            for g in range(len(res)):
                if res[g][-1].end <= interval.start:
                    res[g].append(interval)
                    placed = True
                    break

            if not placed:
                res.append([interval])

        return len(res)