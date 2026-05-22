class Employee:
    def __init__(self,eid,ename,job):
        self.eid=eid
        self.ename=ename
        self.job=job
        print("Employee Id :",self.eid)
        print("Employee Name :",self.ename)
        print("Employee Job :",self.job)

class Department(Employee):
    def __init__(self,deptno,dname,empno,empname,jobname):
        super().__init__(empno,empname,jobname)
        self.deptno=deptno
        self.dname=dname
        print("Department No :",self.deptno)
        print("Department Name:",self.dname)

obj=Department(10,"Accounting",101,"Santosh","Manager")
obj2=Department(20,"Research",102,"Adams","Analyst")
