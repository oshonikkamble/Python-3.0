class Arithmatic:
    
    def __init__(self,value1): 
        self.No1 =value1    
        
    def ChkPrime(self):                       
        flag = 0
        for i in range(2,self.No1):
          if self.No1%i==0:
            flag = 1
            break
        if flag == 1:
          print('Not Prime')
        else:
          print("Prime")

    def ChkPerfect(self):                          
        sum = 0

        for i in range(1, self.No1):
            if self.No1% i == 0:
                sum = sum + i

        if sum == self.No1:
            print("--- Perfect number ---")
        else:
            print("--- Not a Perfect number ---")
            
    def SumFactors(self):   
        s=0
        for i in range(1,self.No1+1):
            if self.No1%i==0:
                s+=i
        print("Sum of factors: ",s)
                    
    def Factors(self):  
        print("Factors : ")
        for x in range (1,self.No1+1):
            if self.No1%x==0:
                print(x , end=" ")        
                
print("Enter first Number ")
A=int(input())

obj = Arithmatic(A)
obj.ChkPrime()
obj.ChkPerfect()
obj.SumFactors()
obj.Factors()
