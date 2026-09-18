class employee():
    def __init__(self,name,employeeid,basicsalary):
        self.name=name
        self.employeeid=employeeid
        self.basicsalary=basicsalary
    def totalsalary(self):
        hra=0.2*self.basicsalary
        da=0.1*self.basicsalary
        ttlsalary=hra+da+self.basicsalary
        print("Totalsalarry:",ttlsalary)
o1=employee("suresh",22,1000)
print("name:",o1.name)
print("emplyeeid:",o1.employeeid)
print("basicsalary:",o1.basicsalary)
o1.totalsalary()