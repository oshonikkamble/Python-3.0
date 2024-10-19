

def Add(No1, No2):
    Ans = No1 + No2
    return Ans

def Sub(No1, No2):
    Ans = No1 - No2
    return Ans

def Mul(No1, No2):
    Ans = No1 * No2
    return Ans

def Div(No1, No2):
    Ans = No1 / No2
    return Ans

def main():
    
    print("Enter The First Number :  ")
    A=int(input())

    print("Enter The Second Number : " )
    B=int(input())

    Result = Add(A, B)
    print("Addition is : ",Result)

    Result = Sub(A, B)
    print("Subtraction is : ",Result)

    Result = Mul(A, B)
    print("Multiplication is : ",Result)

    Result = Div(A, B)
    print("Division is : ",Result)

if __name__ == "__main__":
    main()