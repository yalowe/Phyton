class student:
    grade1=0
    age1=0
    count=0
    def __init__(self,name):
        self.name=name

    def tell_name(self):    
        print('name:',self.name, end=" ")

class age_grad(student):
    def __init__(self,age,grade):

        student.grade1+=grade
        student.age1+=age
        student.count+=1
        self.age=age
        self.grad=grade
        print("age:",self.age,",grade:",self.grad)
        
        
s1=student("Mob,")
s1.tell_name()
s1=age_grad(25,80)


s2=student("Momo,")
s2.tell_name()
s2=age_grad(26,75)


s3=student("Alice,")
s3.tell_name()
s3=age_grad(23,82)

print("avereg of grade:",student.grade1//student.count)
print("avereg of age:",student.age1//student.count)

