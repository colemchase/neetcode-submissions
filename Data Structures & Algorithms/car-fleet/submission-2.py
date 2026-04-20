class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        groups = list(zip(position, speed))
        groups.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for group in groups:
            stack.append((target - group[0]) / group[1])

            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        

        return len(stack)