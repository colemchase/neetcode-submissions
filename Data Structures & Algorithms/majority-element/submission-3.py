class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        cnt = 1

        for num in nums[1:]:
            if num == curr:
                cnt+=1
            else:
                cnt-=1
                if cnt == 0:
                    curr = num
                    cnt+=1

        return curr