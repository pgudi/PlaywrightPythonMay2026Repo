class Department:
    def __init__(self,deptno,dname,loc):
        self.deptno=deptno
        self.dname=dname
        self.loc=loc

    def show_department_details(self):
        print("Dept Number :",self.deptno)
        print("Dept Name :",self.dname)
        print("Location :",self.loc)

obj1=Department(10,"Accounting","Dallas")
obj1.show_department_details()

obj2=Department(20,"Research","California")
obj2.show_department_details()
