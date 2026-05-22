class Maths1:
    def addition(self,x,y):
        result=(x + y)
        print("Addition Result :",result)

class Maths2(Maths1):
    def substraction(self,x,y):
        print("Substraction Result :",(x-y))

class Maths3(Maths2):
    def division(self,a,b):
        print("Division Result :",(a/b))

obj1=Maths3()
obj1.division(100,10)
obj1.substraction(50,35)
obj1.addition(40,30)