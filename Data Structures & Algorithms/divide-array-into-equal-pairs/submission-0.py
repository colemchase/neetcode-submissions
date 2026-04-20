class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        for key in cnt.keys():
            if cnt[key] % 2 != 0:
                return False
        
        return True