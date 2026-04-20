class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        # build
        for iteration in range(len(words)):
            across = words[iteration]

            down = ""
            for r in range(len(across)): 
                if r >= len(words):
                    return False
                if iteration >= len(words[r]):
                    print(iteration, words[r])
                    return False
                down+=words[r][iteration]

            if across != down:
                return False
        return True
            