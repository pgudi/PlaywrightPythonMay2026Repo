class Employee:
    def __init__(self, empno,ename,job,sal):
        self.empid=empno
        self.empname=ename
        self.jobname=job
        self.salary=sal
        print("Empolyee Id :",self.empid)
        print("Empolyee Name :",self.empname)
        print("Empolyee Job :",self.jobname)
        print("Empolyee Salary :",self.salary)
        print("-----------------")

obj1=Employee(101,"Santosh","Manager",25000)
obj2=Employee(102,"Adams","Anayst",15000)
obj3=Employee(103,"Jones","Clerk",18000)

