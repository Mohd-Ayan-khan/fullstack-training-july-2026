class areas:
    def area(self):
        print("area")

class circle(areas):
    def area(self,r):
        result = (r*r) * 3.14
        print(result)
        

class retengle(areas):
    def area(self,l,w):
        result = l*w
        print(result)

obj1 = circle()
obj1.area(10)

obj2 = retengle()
obj2.area(8,9)