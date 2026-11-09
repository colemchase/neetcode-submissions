class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # find hardest level
        # sub armor from hardest level
        # return sum of before hardest level and sum after hardest level, plus 1
        
        hardest_level = 0
        
        for i in range(len(damage)):
            if damage[i] > damage[hardest_level]:
                hardest_level = i

        left = sum(damage[:hardest_level])
        mid = damage[hardest_level] - armor if damage[hardest_level] > armor else 0
        right = sum(damage[hardest_level+1:]) + 1
        
        return left + mid + right
