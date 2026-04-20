class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # make a window
        window = sum(arr[:k])

        # find the average, res += if threshold
        res = 1 if window / k >= threshold else 0

        # loop through arr from next index
        for i in range(1, len(arr)-k+1):
            # add new number 
            window += arr[i+k-1]
            # delete old number
            window -= arr[i-1]
            # res +=1 if threshold
            res += 1 if window / k >= threshold else 0
        
        return res