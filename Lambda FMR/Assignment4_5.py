CheckNum =lambda No : all( (No%i != 0) for i in range(2, int(No**.5)+1)) 
Multiply = lambda No: No * 2
Max = lambda A, B: A if A > B else B

def filterX(Task, Elements):
    Result = []   

    for no in Elements:
        Ret = Task(no)
        if Ret:
            Result.append(no)
            
    return Result

def mapX(Task, Elements):
    Result = []
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    
    return Result

def reduceX(Task, Elements):
    result = Elements[0]
    for item in Elements:
        result = Task(result, item)
    return result

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        No = int(input())
        Data.append(No)    
        
    print("Data from input list : ", Data)
    FData = filterX(CheckNum, Data)
    print("Data after filter activity : ", FData)

    MData = mapX(Multiply, FData)
    print("Data after map activity : ", MData)

    try:
        RData = reduceX(Max, MData)
        print("Data after reduce activity is : ", RData)
    except IndexError:
        print("No elements to reduce")

if __name__ == "__main__":
    main()