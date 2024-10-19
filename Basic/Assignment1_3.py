
def Add(No1, No2):
   Ans = No1 + No2
   return Ans

def main():
   print("Enter the 1st Number : ")
   A=int(input())

   print("Enter the 2nd Number : ")
   B=int(input())

   Result = Add(A,B)

   print("Addition is : ",Result)

if __name__ == "__main__":
    main()
