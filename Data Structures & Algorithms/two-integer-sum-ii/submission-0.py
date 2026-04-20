class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(numbers):
            diff = target - num

            if diff != num and diff in hm:
                return [hm[diff]+1, i+1]
            if num not in hm:
                hm[num] = i
        
                