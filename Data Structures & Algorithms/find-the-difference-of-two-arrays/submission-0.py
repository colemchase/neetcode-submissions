class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = set(nums1)
        n2 = set(nums2)

        res = [[], []]

        for num in n1:
            if num not in n2:
                res[0].append(num)
        
        for num in n2:
            if num not in n1:
                res[1].append(num)
        
        return res