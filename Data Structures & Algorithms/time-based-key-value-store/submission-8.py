class TimeMap:

    def __init__(self):
        self.times = {} # key -> [ (timestamp, value), (timestamp, value), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []
        self.times[key].append((timestamp, value))

    def bs(self, key, ts, l, h):

        if l >= h: # base case
            if l < len(self.times[key]) and self.times[key][l][0] <= ts: # we found it
                return self.times[key][l][1]

            return self.times[key][l-1][1] if l > 0 else ""
        
        mid = ((h-l) // 2) + l
        
        if self.times[key][mid][0] < ts:
            return self.bs(key, ts, mid+1, h)
        elif self.times[key][mid][0] > ts:
            return self.bs(key, ts, l, mid-1)
        return self.times[key][mid][1]
            

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.times:
            return ""

        return self.bs(key, timestamp, 0, len(self.times[key])-1)
        


