class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = {}
        res = set()
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num]+=1
            if hm[num] > len(nums)//3:
                res.add(num)

        return list(res)