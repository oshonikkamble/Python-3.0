def Mul(A,B):
    Ans = 0
    Ans = A * B
    return Ans

A = lambda A,B : A * B

def main():
    print("Enter 1st Number : ")
    A=int(input())

    print("Enter 2nd Number  :  ")
    B=int(input())
    ret = Mul(A,B)
    Mul(A,B)
    print("Multiplication is :  ",ret)

if __name__ == "__main__":
    main()