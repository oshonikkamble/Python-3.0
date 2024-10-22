
def Accept(No):
    if(No % 5 == 0):
        print(True)
    else:
        print(False)

def main():
    print("Enter the Number : ")
    
    A = int(input())

    Accept(A)

if __name__ == "__main__":
    main()
