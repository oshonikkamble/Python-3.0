CheckNum = lambda No : (No >= 70) and (No <= 90)
Increase = lambda No : No + 10
Mul = lambda A, B : A * B

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
    if len(Elements) == 0:  
        return None
    result = Elements[0]
    for no in Elements[1:]:
        result = Task(result, no)
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

    MData = mapX(Increase, FData)
    print("Data after map activity : ", MData)

    RData = reduceX(Mul, MData)
    if RData is not None:
        print("Data after reduce activity is : ", RData)
    else:
        print("No elements to reduce")

if __name__ == "__main__":
    main()