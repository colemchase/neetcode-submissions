class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr)//2
            l = merge(arr[:mid])
            r = merge(arr[mid:])
            res = []
            i = 0
            j = 0

            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    res.append(l[i])
                    i+=1
                else:
                    res.append(r[j])
                    j+=1

            if i != len(l):
                res+=l[i:]
            if j != len(r):
                res+=r[j:]

            return res

        return merge(nums)