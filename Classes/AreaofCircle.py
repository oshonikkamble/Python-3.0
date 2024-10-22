class Circle:
    Pi=3.14 

    def __init__(self,radius): 
        self.radius = radius
           
    def Area(self):                       
        Ans = Circle.Pi * self.radius * self.radius
        return Ans

    def Circumference(self):                          
        Ans = 2* Circle.Pi * self.radius
        return Ans
    

print("Enter Radius ")
radius=float(input())

obj = Circle(radius)

Ret = obj.Area()
print("Area is : ",Ret)

Ret = obj.Circumference()
print("Circumference is : ",Ret)

