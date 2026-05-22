class Department:
    def __init__(self):
        self.deptno=10
        self.dname="Sales"
        self.loc="California"

    def show_department_details(self):
        print("Dept Number :",self.deptno)
        print("Dept Name :",self.dname)
        print("Location :",self.loc)

obj=Department()
obj.show_department_details()

obj2=Department()
obj2.show_department_details()



