
sum = 0

def Summation(No): 
    global sum
    if(No != 0):
   
        sum = sum + (No % 10)
        No = No // 10
        Summation(No)
    
    return sum
    

def main():

    print("Enter Number : ")
    No = int(input())    
 
 
    print("Summation of Digits : ",Summation(No))

if __name__ == "__main__":
    main()

