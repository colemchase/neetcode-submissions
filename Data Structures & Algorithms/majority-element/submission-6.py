class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = nums[0]
        res_count = 1

        for num in nums[1:]:
            if num == res:
                res_count += 1
            else:
                res_count -= 1
                if res_count == 0:
                    res = num
                    res_count += 1

        
        return res