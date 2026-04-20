class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # loop through c in s
        for c in s:

            # if opening brack, append to stack
            if c == "(" or c == "{" or c == "[":
                stack.append(c)

            else: # if closing brack, make sure it matches top of stack
                if len(stack) > 0:
                    matches = False
                    top = stack[-1]
                    match c:
                        case ")":
                            if top == "(":
                                matches = True
                        case "}":
                            if top == "{":
                                matches = True
                        case "]":
                            if top == "[":
                                matches = True
                    if not matches:
                        return False
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

            

