class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # int(//)

        stacky = []
        for token in tokens:
            match token:
                case "+":
                    r = int(stacky.pop())
                    l = int(stacky.pop())
                    stacky.append(int(l + r))
                case "*":
                    r = int(stacky.pop())
                    l = int(stacky.pop())
                    stacky.append(int(l * r))
                case "/":
                    r = int(stacky.pop())
                    l = int(stacky.pop())
                    stacky.append(int(l / r))
                case "-":
                    r = int(stacky.pop())
                    l = int(stacky.pop())
                    stacky.append(int(l - r))
                case _:
                    stacky.append(int(token))
        
        return stacky[0]