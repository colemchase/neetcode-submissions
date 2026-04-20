class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hm = {}
        self.nums = nums
        for num in nums:
            if num not in self.hm:
                self.hm[num] = 0
            self.hm[num] += 1

    def showFirstUnique(self) -> int:
        for num in self.nums:
            if self.hm[num] == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        if value not in self.hm:
            self.hm[value] = 0
        self.hm[value]+=1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
