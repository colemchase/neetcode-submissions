class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        for i in range(len(nums1)):
            curr = nums1[i]
            position = -1
            for j, item in enumerate(nums2):
                if item == curr:
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > item:
                            position = nums2[k]
                            break
                    break
            nums1[i] = position

        return nums1