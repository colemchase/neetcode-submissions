class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.left = [0]


        for num in nums:
            self.left.append(self.left[-1] + num)


    def sumRange(self, l: int, r: int) -> int:
        return self.left[r+1] - (self.left[l] - self.left[0])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)