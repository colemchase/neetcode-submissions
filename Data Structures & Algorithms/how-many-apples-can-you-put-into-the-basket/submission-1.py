class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()

        res = 0
        total_weight = 0

        for apple in weight:
            total_weight += apple
            if total_weight <= 5000:
                res+=1
            else:
                break

        return res
