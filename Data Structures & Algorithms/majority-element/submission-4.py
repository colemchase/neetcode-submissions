class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        res_count = 0
        
        for key in counter.keys():
            if counter[key] > res_count:
                res_count = counter[key]
                res = key
        
        return res