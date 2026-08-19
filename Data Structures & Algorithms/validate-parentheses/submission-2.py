class Solution:
    def isValid(self, s: str) -> bool:
        # () { } []

        # Stack
        stacy = []

        for p in s:
            if p == "(" or p == "{" or p == "[":
                stacy.append(p)
            else:
                if not stacy:
                    return False
                
                if stacy[-1] == "(" and p == ')':
                    stacy.pop()
                elif stacy[-1] == "{" and p == '}':
                    stacy.pop()
                elif stacy[-1] == "[" and p == ']':
                    stacy.pop()
                else:
                    return False
        
        return len(stacy) == 0