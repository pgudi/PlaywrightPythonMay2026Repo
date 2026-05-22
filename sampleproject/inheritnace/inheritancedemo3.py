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

obj1=Maths2()
obj1.substraction(40,20)
obj1.addition(50,60)

obj2=Maths3()
obj2.division(40,5)
obj2.addition(100,40)
