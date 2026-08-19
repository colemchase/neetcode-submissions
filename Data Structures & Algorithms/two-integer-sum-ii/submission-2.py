class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brutal 
        # double for loop, O(n^2)
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]

        # Optimal
        # O(n)
        hm = {}
        for i, num in enumerate(numbers):
            diff = target-num
            if diff in hm:
                return [hm[diff]+1, i+1]
            hm[num] = i

