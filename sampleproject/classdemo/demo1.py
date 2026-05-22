class Person:
    def __init__(self):
        print("It is No Args Constructor!!!!")

    def __init__(self,fname):
        print("First Parameter :",fname)

# o1=Person()
o2=Person("Testing")