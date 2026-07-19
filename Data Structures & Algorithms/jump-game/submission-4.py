class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # find jump that when landing, then goes furthest

        i = 0

        while i < len(nums)-1:
            if nums[i] == 0:
                return False

            winner = i+1
            dist = 0
            for jump in range(i+1, i+nums[i]+1):
                if jump >= len(nums):
                    return True
                curr = nums[jump] + jump
                if curr > dist:
                    winner = jump
                    dist = curr
                
            i = winner
        return True