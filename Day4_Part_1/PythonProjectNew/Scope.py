class ScopeExample:
    __privateString="Prasanna"
    _protectedSting="Nissy"
    publicString="Great Learning"

    def getPrivateData(self):
        return self.__privateString

    def getProtectedData(self):
        return self._protectedSting

ex=ScopeExample()
print(ex.publicString)
print(ex.getPrivateData())
print(ex.getProtectedData())