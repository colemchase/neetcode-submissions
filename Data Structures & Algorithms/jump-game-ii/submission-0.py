class Solution:
    def jump(self, nums: List[int]) -> int:
        hm = {}

        def jumper(i):
            if i in hm: # already been here
                return hm[i]

            if i >= len(nums)-1: # success
                hm[i] = 1
                return hm[i]
            
            dist = nums[i]
            if dist == 0: # dead end
                hm[i] = 0
                return hm[i]

            winner = float('inf')
            for jump in range(i+1, i + nums[i]+1): # go through candidates 
                curr = jumper(jump)
                curr += 1 if curr else 0
                print(curr)
                winner = min(winner, curr) if curr else winner
            
            if winner != float('inf'):
                hm[i] = winner
                return hm[i]
                    
            hm[i] = 0
            return hm[i]

        jumper(0)

        return hm[0] - 1