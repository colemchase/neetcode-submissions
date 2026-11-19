class WordDictionary:

    def __init__(self):
        self.isWord = False
        self.children = {}


    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.isWord = True


    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c not in curr.children:
                if c == ".":
                    for c in curr.children.keys():
                        if curr.children[c].search(word[i+1:]):
                            return True
                return False
            curr = curr.children[c]
        return curr.isWord
