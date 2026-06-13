class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        total =  sum(matchsticks)
        target = total // 4

        if total / 4 != target:
            return False

        sides = [0, 0, 0, 0]
        
        matchsticks.sort(reverse=True)
        
        def backtrack(i):

            if i == len(matchsticks): # all sides lined up successfully
                return True

            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
                
            return False
            
        return backtrack(0)
            

                