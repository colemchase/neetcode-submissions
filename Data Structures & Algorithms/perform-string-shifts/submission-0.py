class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        def left(s, x):
            x %= len(s)
            return s[x:] + s[:x]
        
        def right(s, x):
            x = x % len(s)
            return s[len(s)-x:] + s[:len(s)-x]
        
        for sh in shift:
            if sh[0] == 0:
                s = left(s, sh[1])
            else:
                s = right(s, sh[1])
        
        return s