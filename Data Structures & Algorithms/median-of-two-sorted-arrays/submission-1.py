class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # double heaps (left max heap, right min heap)
        # insert to appropriate side base on comparison of top of each side
        # if size of left compare to right is greater than 1, pop left and push to right

        left = []
        right = []
        heapq.heapify(left)
        heapq.heapify(right)

        for num in nums1 + nums2:
            if left and right and num > right[0]:
                heapq.heappush(right, num)
            else:
                heapq.heappush(left, -num)


            # rebalance
            if len(left) - len(right) > 1:
                heapq.heappush(right, -heapq.heappop(left))
            if len(right) - len(left) > 1:
                heapq.heappush(left, -heapq.heappop(right))


        if len(right):
            if len(left) > len(right): # has right and odds size of nums
                return -heapq.heappop(left)
            elif len(right) > len(left):
                return heapq.heappop(right)
            return (-heapq.heappop(left) + heapq.heappop(right)) / 2 # has right and even size of nums

        return -heapq.heappop(left) # no right