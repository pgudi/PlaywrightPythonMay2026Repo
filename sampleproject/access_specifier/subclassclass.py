from protectionclass import Protection

class SubClass(Protection):
    def __init__(self):
        super().__init__()
        print("Execution of SubClass class constructor!!!")
        print("Public Variable :",self.publicvariable)
        print("Protected Variable :",self._protectedvariable)
        # print("Private Variable :",self.__privatevariable)
        print("--------------------------")

    