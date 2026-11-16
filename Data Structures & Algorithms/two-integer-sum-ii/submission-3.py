class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # already sorted!
        # 1 indexed
        # return two indexs, nums at those indexs should add to equal target 
        # indexes cannot be equal

        # two pointer approach
        l = 0
        r = len(numbers)-1

        while l < r:
            curr = numbers[l] + numbers[r]

            if curr < target:
                l+=1
            elif curr > target:
                r-=1
            else:
                return [l+1, r+1]
        
        



