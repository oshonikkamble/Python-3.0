def Addition(No): 
    sum = 0
    while (No != 0): 
       
        sum = sum + (No % 10)
        No = No // 10
       
    return sum
   
def main():

    print("Enter Number : ")
    No = int(input())    
 
    Addition(No)
    print("Addition of Digits : ",Addition(No))

if __name__ == "__main__":
    main()

