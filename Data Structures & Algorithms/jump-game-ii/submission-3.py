class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        i = 0
        while True:
            
            if i >= len(nums)-1: # success
                return jumps

            dist = 1
            for jump in range(i+1, i + nums[i]+1): # go through candidates 
                if jump >= len(nums)-1:
                    return jumps+1
                curr = jump + nums[jump]
                dist = max(curr, dist)
            i = dist
            jumps += 2
            