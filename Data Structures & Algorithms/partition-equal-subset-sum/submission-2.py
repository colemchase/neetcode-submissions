class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # find sum // 2? 

        total = sum(nums) 
        if total % 2: # cant split odds
            return False 

        target = total // 2

    
        dp = {}

        def backtracking(i, curr):
            if (i, curr) in dp: # already seen
                return dp[(i, curr)]
            if i == len(nums): # end of list
                dp[(i, curr)] = curr == 0
                return dp[(i, curr)]
            if curr == 0: # solution
                dp[(i, curr)] = True
                return dp[(i, curr)]
            
            if backtracking(i+1, curr-nums[i]) or backtracking(i+1, curr):
                dp[(i, curr)] = True
            else:
                dp[(i, curr)] = False
            return dp[(i, curr)]

        backtracking(0, target)

        return dp[(0, target)]