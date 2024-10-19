def MinNum():

    print("Enter the elements: ")
    size= int(input())

    A = list()
    print("Enter the Number :")
        
    for i in range(size):
        b=int(input())
        A.append(b)
       
    print("Enter the Elements Are: ",A)
    
    Result = min(A)

    print("Minimum Number is : ", Result)
    
MinNum()
