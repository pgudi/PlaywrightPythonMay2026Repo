class Maths1:
    def addition(self,x,y):
        result=(x + y)
        print("Addition Result :",result)

class Maths2:
    def substraction(self,x,y):
        print("Substraction Result :",(x-y))

class Maths3(Maths1,Maths2):
    def division(self,a,b):
        print("Division Result :",(a/b))

obj=Maths3()
obj.division(30,15)
obj.substraction(20,4)
obj.addition(15,35)