 
def Factorial(No):
    fact = 1
    
    if (No >= 1):
        
        for i in range (1, No + 1):
            
            fact = fact *i

        print("Factorial of the given number is: ", fact)

def main():

    print("Enter Number : ")
    A = int(input())
    
    Factorial(A)

if __name__ == "__main__":
    main()
