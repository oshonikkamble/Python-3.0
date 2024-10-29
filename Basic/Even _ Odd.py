
def ChkNum(No):
    
    if(No % 2 == 0):
        print(" Even Number ")
    else:
        print(" Odd Number ")

def main():
    print("Enter the Number : ")
    A = int(input())

    ChkNum(A)
if __name__ =="__main__":
    main()
