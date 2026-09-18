class student():
    def __init__(self,name,rollno,sub1,sub2,sub3):
        self.name=name
        self.rollno=rollno
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    def totalmarks(self):
        totalmarks=self.sub1+self.sub2+self.sub3
        return totalmarks
    def average(self):
         self.avg=self.totalmarks()/3
         return self.avg
    def grade(self):
        self.avg = self.average() 
       
        if(self.avg>=90):
            print("grade:A")
        elif(self.avg>=75 and self.avg<90):
            print("grade:B")
        elif(self.avg>=60 and self.avg<75):
            print("grade : c")
        else:
            print("Fail")
            
r=student("suresh",22,90,80,75)
print("Enter Name:",r.name)
print("Enter Rollno:",r.rollno)
print("Enter sub1:",r.sub1)
print("Enter sub2:",r.sub2)
print("Enter sub3:",r.sub3)
print("totalmarls:",r.totalmarks)
print("Average:", r.average())
r.grade()