class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacky = []
        

        for token in tokens:

            match token:
                case "+":
                    r = stacky.pop()
                    l = stacky.pop()
                    stacky.append(l+r)
                case "-": 
                    r = stacky.pop()
                    l = stacky.pop()
                    stacky.append(l-r)
                case "*":
                    r = stacky.pop()
                    l = stacky.pop()
                    stacky.append(l*r)
                case "/":
                    r = stacky.pop()
                    l = stacky.pop()
                    stacky.append(int(l/r))
                case _:
                    stacky.append(int(token))

        return stacky[0]