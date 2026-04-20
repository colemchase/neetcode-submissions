class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        for i in range(len(arrays)):
            arrays[i] = (arrays[i][0], arrays[i][-1])
        
        arrays.sort(key=lambda x: x[0])
        for i in range(len(arrays)):
            arrays[i] = (i, arrays[i][0], arrays[i][1])
        
        backward = arrays.copy()
        backward.sort(key=lambda x: x[2], reverse=True)
      
        def dive(l, r):
            if l < len(arrays) and r < len(arrays):
                lval = arrays[l][1]
                li = arrays[l][0]
                rval = backward[r][2]
                ri = backward[r][0]
                if ri != li:
                    return rval-lval
                return max(dive(l+1,r), dive(l, r+1))
            return 0
            
        return dive(0, 0)
