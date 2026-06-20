
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        for c in word:
            if c not in self.children:
                self.children[c] = TrieNode()
            self = self.children[c]
        self.isWord = True

    def search(self, word):
        # if on the last c return isWord
        if len(word) == 0:
            return self.isWord

        if word[0] == ".":
            for k in self.children.keys():
                temp = self.children[k].search(word[1:])
                if temp:
                    return True
            return False
        else:
            if word[0] in self.children:
                return self.children[word[0]].search(word[1:])
        return False
        


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        self.root.addWord(word)

    def search(self, word: str) -> bool:
        return self.root.search(word)
