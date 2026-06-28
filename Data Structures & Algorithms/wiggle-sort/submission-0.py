class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mnheap = []

        for num in nums:
            heapq.heappush(mnheap, num)
        
        for i in range(0, len(nums), 2):
            nums[i] = heapq.heappop(mnheap)
        
        for i in range(1, len(nums), 2):
            nums[i] = heapq.heappop(mnheap)
        
        