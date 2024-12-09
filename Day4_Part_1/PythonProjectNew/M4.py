class Test:
    def __init__(self,privateStr,protectedStr,publicStr):
        self.__privateStr=privateStr
        self._protectedStr=protectedStr
        self.publicStr = publicStr

test=Test("privateHi","protectedTest","publicDemo")
print(test.publicStr)