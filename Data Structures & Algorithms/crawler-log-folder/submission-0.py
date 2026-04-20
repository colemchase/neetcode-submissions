class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0 # stack
        # loop through each log
        for log in logs:
            match log: # make decision of how to adjust stack
                case "../": # decrement the level unless 0 
                    level -= 1 if level != 0  else 0
                case "./": # do nothing, neceassry for wildcard option
                    continue
                case _:
                    level += 1
        
        return level