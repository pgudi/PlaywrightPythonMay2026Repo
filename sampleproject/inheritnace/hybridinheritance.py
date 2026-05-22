class Maths1:
    def addition(self,x,y):
        result=(x + y)
        print("Addition Result :",result)

class Maths2(Maths1):
    def substraction(self,x,y):
        print("Substraction Result :",(x-y))

class Maths3(Maths1):
    def division(self,a,b):
        print("Division Result :",(a/b))

class Maths4(Maths3):
    def multiplication(self,a,b):
        print("Multiplication Result:",(a * b))

obj1=Maths2()
obj1.substraction(100,70)
obj1.addition(10,30)

obj2=Maths4()
obj2.multiplication(14,10)
obj2.division(45,5)
obj2.addition(30,60)

