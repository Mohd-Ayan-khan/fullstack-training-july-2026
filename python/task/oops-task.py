class student:
    
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        print("name is :",self.name)
        print("age is :", self.age)
        print("grade is :", self.grade)
    
    
obj = student("ayan",48,"B")
obj1 = student("rehan",23,"A")

print("===================")    
obj.display()
print("===================")    
obj1.display()
print("===================")    
