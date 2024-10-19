def Frequency():
    
    print("Enter the number of elements: ")
    n = int(input())
    
    A= list()
    print("Numbers : ")

    for i in range(n):
        no=int(input())
        A.append(no)

    print("List of numbers:", A)

    
    print("Enter the number to find in list: ")
    search_num = int(input())
    
    frequency = A.count(search_num)
    print("Frequency of", search_num, "in the list:", frequency)

Frequency()
