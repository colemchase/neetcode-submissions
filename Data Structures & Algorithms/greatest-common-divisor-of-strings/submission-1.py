class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def cmpDiv(curr, s):
            if len(s) % len(curr) == 0:
                # check if not divisor of strings to skip
                for j in range(0, len(s), len(curr)):
                    if s[j:j+len(curr)] != curr:
                        return False
            else:
                return False
            return True
                
        for i in range(len(min(str1, str2)), 0, -1):
            curr = str1[:i]
            # check for divisiablity
            if not cmpDiv(curr, str1):
                continue
            if not cmpDiv(curr, str2):
                continue
            return curr
        
        return ""