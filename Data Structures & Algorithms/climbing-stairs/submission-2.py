class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        def climb():
            if len(steps) >= n:
                return steps[n-1]
            steps.append(steps[-1] + steps[-2])
            return climb()
            
        return climb()