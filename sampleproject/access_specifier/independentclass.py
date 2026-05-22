from protectionclass import Protection

class Independent:
    def __init__(self):
        o=Protection()
        print("Execution of Protection class constructor!!!")
        print("Public Variable :",o.publicvariable)
        print("Protected Variable :",o._protectedvariable)
        # print("Private Variable :",o.__privatevariable)
        print("--------------------------")