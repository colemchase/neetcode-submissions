class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        indexer = {}
        for i, item in enumerate(nums2):
            indexer[item] = i
        print(indexer)
        for i in range(len(nums1)):
            curr = nums1[i]
            position = -1
            if curr in indexer:
                j = indexer[curr]
                for k in range(j+1, len(nums2)):
                    if nums2[k] > curr:
                        position = nums2[k]
                        break
            nums1[i] = position

        return nums1