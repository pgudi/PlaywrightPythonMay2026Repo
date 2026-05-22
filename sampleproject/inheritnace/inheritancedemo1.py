class Maths1:
    def addition(self,x,y):
        result=(x + y)
        print("Addition Result :",result)

class Maths2(Maths1):
    def substraction(self,x,y):
        print("Substraction Result :",(x-y))

obj1=Maths2()
obj1.substraction(10,5)
obj1.addition(30,10)