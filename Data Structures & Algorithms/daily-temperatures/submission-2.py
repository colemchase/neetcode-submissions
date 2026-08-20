class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stacy = [] # [temp, index]
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stacy and temp > stacy[-1][0]:
                end_temp, end_i = stacy.pop()
                res[end_i] = i-end_i
            # no stack or temp < end of stacy
            stacy.append((temp, i))
            
        return res

