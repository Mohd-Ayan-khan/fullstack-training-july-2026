class person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print("hello my name is :",self.name)
    
obj = person("ayan",34)

obj.greet()