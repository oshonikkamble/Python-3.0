class Arithmatic:
    def __init__(self,value1,value2): 
        self.No1 =value1    
        self.No2=value2   
        
    
    def Addition(self):                       
        Ans = self.No1 + self.No2
        return Ans

    def Subtraction(self):                          
        Ans = self.No1 - self.No2
        return Ans

    def Multiplication(self):                         
        Ans = self.No1 * self.No2
        return Ans

    def Division(self):                          
        Ans = self.No1 / self.No2
        return Ans

print("Enter first Number ")
A=int(input())

print("enter second number")
B = int(input())

obj = Arithmatic(A,B)

Ret = obj.Addition()
print("Addition is : ",Ret)

Ret = obj.Subtraction()
print("Subtraction is : ",Ret)

Ret = obj.Multiplication()
print("Multiplication is : ",Ret)

Ret = obj.Division()
print("Division is : ",Ret)