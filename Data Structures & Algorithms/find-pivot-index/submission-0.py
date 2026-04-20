class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = [0]
        for num in nums:
            l.append(num+l[-1])
        l.pop(0)

        r = [0]
        for num in nums[::-1]:
            r.append(num+r[-1])
        r.pop(0)
        r = r[::-1]

        for i in range(len(r)):
            if r[i] == l[i]:
                return i

        return -1