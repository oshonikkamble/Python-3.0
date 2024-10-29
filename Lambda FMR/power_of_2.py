
def Power(No):
    Ans =0
    Ans= 2 ** No     
    return Ans

A = lambda No : 2 ** No    

def main():
    print("enter the number : ")
    No=int(input())

    ret=Power(No)
    Power(No)
    print("Power of 2 is : ",ret)

if __name__ == "__main__":
    main()
