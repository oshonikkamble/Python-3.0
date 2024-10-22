def CheckNum(No):
    
    if(No > 0):
        print(" Positive Number ")
    elif (No == 0):
        print(" Zero ")
    else:
        print(" Negative Number ")

def main():
    print("Enter the Number : ")
    A = int(input())

    CheckNum(A)

if __name__ == "__main__":
    main()
