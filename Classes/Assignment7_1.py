
class Demo:
    Data = 11

    def __init__(self, A, B):   
        
        self.No1 = A    
        self.No2 = B    

    def Fun(self):  
        print("Value of No1 from dipslay : ",self.No1)
        print("Value of No2 from dipslay : ",self.No2)
        print("Value of Data from dipslay : ",Demo.Data)
       

    def Gun(self):  
        print("Value of No1 from dipslay : ",self.No1)
        print("Value of No2 from dipslay : ",self.No2)
        print("Value of Data from dipslay : ",Demo.Data)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

print("Values of No1 from obj1 : ",obj1.No1)
print("Values of No2 from obj1 : ",obj1.No2)

print("Values of No1 from obj2 : ",obj2.No1)
print("Values of No2 from obj2 : ",obj2.No2)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
