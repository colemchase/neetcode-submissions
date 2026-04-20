class StringIterator:

    def __init__(self, compressedString: str):
        linster = []
        for c in compressedString:
            if c.isalpha():
                linster.append(c)
            else:
                if linster[-1].isnumeric():
                    linster[-1]+=c
                else:
                    linster.append(c)
        print(linster)
        for i in range(len(linster)):
            if linster[i][0].isnumeric():
                linster[i] = int(linster[i])
        self.linster = linster
        self.index = 0

        

    def next(self) -> str:
        if self.hasNext():
            res = self.linster[self.index] 
            self.linster[self.index+1] -= 1
            if self.linster[self.index+1] == 0:
                self.index+=2
            return res
        return " "
            
            
                

    def hasNext(self) -> bool:
        return self.index < len(self.linster)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
