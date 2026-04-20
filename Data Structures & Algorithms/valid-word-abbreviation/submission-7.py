class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = j = 0
        while i < len(word) and j < len(abbr):
            if word[i] != abbr[j]:
                if abbr[j].isnumeric():
                    num = abbr[j]
                    if num != "0":
                        k = 1
                        while j+k < len(abbr) and abbr[j+k].isnumeric():
                            num += abbr[j+k]
                            k+=1
                        i+=int(num)
                        j+=k
                        continue
                    else:
                        return False
                else:
                    return False
            i+=1
            j+=1

        return i == len(word) and j == len(abbr)
            