
def outer_example():
    num=200
    def inner_example():
        str="Welcome"
        print("Inside inner function :",num)
    print("the value of str :",str)
    inner_example();

outer_example()

