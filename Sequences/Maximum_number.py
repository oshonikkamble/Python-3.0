def MaxNum():

    print("Enter The Elements:  ")
    size= int(input())

    A= list()
    print("Numbers : ")

    for i in range(size):
        no=int(input())
        A.append(no)

    print("Enter Elements are : ",A)

    Result = max(A)

    print("Maximum No is  : ",Result)

MaxNum()
