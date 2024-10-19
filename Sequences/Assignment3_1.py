def Addition(No):
    sum=0
    for no in No:
        sum = sum + no
    
    return sum

def main():

    print("Enter The Elements:  ")
    size= int(input())

    A= list()
    print("Numbers : ")

    for i in range(size):
        no=int(input())
        A.append(no)

    print("Enter Elements are : ",A)

    Result = Addition(A)

    print("Addition of list is : ",Result)

if __name__ == "__main__":
    main()