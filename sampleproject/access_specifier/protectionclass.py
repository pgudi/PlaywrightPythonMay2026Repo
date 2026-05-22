class Protection:
    def __init__(self):
        self.publicvariable=100
        self._protectedvariable=200
        self.__privatevariable=300
        print("Execution of Protection class constructor!!!")
        print("Public Variable :",self.publicvariable)
        print("Protected Variable :",self._protectedvariable)
        print("Private Variable :",self.__privatevariable)
        print("--------------------------")